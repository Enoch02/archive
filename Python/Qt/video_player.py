"""Multimedia player example"""
import sys
from PyQt6.QtCore import QStandardPaths, Qt, QUrl
from PyQt6.QtGui import QAction, QIcon, QKeySequence, QScreen
from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QFileDialog,
    QMainWindow,
    QSlider,
    QStyle,
    QToolBar,
)
from PyQt6.QtMultimedia import QAudio, QAudioOutput, QMediaFormat, QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget

AVI = "video/x-msvideo"  # AVI
MP4 = "video/mp4"


# TODO: Try to fix this program. The playlists do not work
def get_supported_mime_types():
    result = []

    for f in QMediaFormat().supportedFileFormats(QMediaFormat.ConversionMode.Decode):
        mime_type = QMediaFormat(f).mimeType()
        result.append(mime_type.name())

    return result


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Video Player")

        self._playlist = []
        self._playlist_index = -1
        self._audio_output = QAudioOutput()
        self._player = QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)

        self._player.errorOccurred.connect(self._player_error)

        self.setupToolBar()
        self.setUpMainWindow()

    def setUpMainWindow(self):
        self._video_widget = QVideoWidget()
        self._player.playbackStateChanged.connect(self.update_buttons)
        self._player.setVideoOutput(self._video_widget)

        self.update_buttons(self._player.playbackState)
        self._mime_types = []

        self.setCentralWidget(self._video_widget)

    def setupToolBar(self):
        tool_bar = QToolBar()
        self.addToolBar(tool_bar)

        # file menu
        file_menu = self.menuBar().addMenu("&File")

        icon = QIcon.fromTheme("document-open")
        open_action = QAction(icon, "&Open...", self)
        open_action.setShortcut(QKeySequence.StandardKey.Open)
        open_action.triggered.connect(self.open)

        icon = QIcon.fromTheme("application-exit")
        exit_action = QAction(icon, "E&xit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)

        file_menu.addAction(open_action)
        file_menu.addAction(exit_action)

        # play menu
        play_menu = self.menuBar().addMenu("&Play")

        style = self.style()
        icon = QIcon.fromTheme(
            "media-playback-start.png",
            style.standardIcon(QStyle.StandardPixmap.SP_MediaPlay),
        )
        self._play_action = tool_bar.addAction(icon, "Play")
        self._play_action.triggered.connect(self._player.play)

        icon = QIcon.fromTheme(
            "media-skip-backward-symbolic.svg",
            style.standardIcon(QStyle.StandardPixmap.SP_MediaSkipBackward),
        )
        self._previous_action = tool_bar.addAction(icon, "Previous")
        self._previous_action.triggered.connect(self.previous_clicked)

        icon = QIcon.fromTheme(
            "media-playback-pause.png",
            style.standardIcon(QStyle.StandardPixmap.SP_MediaPause),
        )
        self._pause_action = tool_bar.addAction(icon, "Pause")
        self._pause_action.triggered.connect(self._player.pause)

        icon = QIcon.fromTheme(
            "media-skip-forward-symbolic.svg",
            style.standardIcon(QStyle.StandardPixmap.SP_MediaSkipForward),
        )
        self._next_action = tool_bar.addAction(icon, "Next")
        self._next_action.triggered.connect(self.next_clicked)

        icon = QIcon.fromTheme(
            "media-playback-stop.png",
            style.standardIcon(QStyle.StandardPixmap.SP_MediaStop),
        )
        self._stop_action = tool_bar.addAction(icon, "Stop")
        self._stop_action.triggered.connect(self._ensure_stopped)

        play_menu.addAction(self._play_action)
        play_menu.addAction(self._previous_action)
        play_menu.addAction(self._pause_action)
        play_menu.addAction(self._next_action)
        play_menu.addAction(self._stop_action)

        self._volume_slider = QSlider()
        self._volume_slider.setOrientation(Qt.Orientation.Horizontal)
        self._volume_slider.setMinimum(0)
        self._volume_slider.setMaximum(100)
        available_width = self.screen().availableGeometry().width()
        self._volume_slider.setFixedWidth(int(available_width / 10))
        self._volume_slider.setValue(int(self._audio_output.volume()))
        self._volume_slider.setTickInterval(10)
        self._volume_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self._volume_slider.setToolTip("Volume")
        self._volume_slider.valueChanged.connect(self._audio_output.setVolume)

        tool_bar.addWidget(self._volume_slider)

        about_menu = self.menuBar().addMenu("&About")
        about_qt_act = QAction("About &Qt", self)
        about_qt_act.triggered.connect(QApplication.aboutQt)
        about_menu.addAction(about_qt_act)

    def closeEvent(self, event):
        self._ensure_stopped()
        event.accept()

    def open(self):
        self._ensure_stopped()
        file_dialog = QFileDialog(self)

        is_windows = sys.platform == "win32"
        if not self._mime_types:
            self._mime_types = get_supported_mime_types()

            if is_windows and AVI not in self._mime_types:
                self._mime_types.append(MP4)
            elif MP4 not in self._mime_types:
                self._mime_types.append(MP4)

        file_dialog.setMimeTypeFilters(self._mime_types)

        default_mimetype = AVI if is_windows else MP4
        if default_mimetype in self._mime_types:
            file_dialog.selectMimeTypeFilter(default_mimetype)

        movies_location = QStandardPaths.writableLocation(
            QStandardPaths.StandardLocation.MoviesLocation
        )
        file_dialog.setDirectory(movies_location)

        if file_dialog.exec() == QDialog.DialogCode.Accepted:
            url = file_dialog.selectedUrls()[0]
            self._playlist.append(url)
            self._playlist_index = len(self._playlist) - 1
            self._player.setSource(url)
            self._player.play()

    def _ensure_stopped(self):
        if self._player.playbackState() != QMediaPlayer.PlaybackState.StoppedState:
            self._player.stop()
            self._video_widget.repaint()

    def previous_clicked(self):
        """Go to previous track if we are within the first 5 seconds of
        playback otherwise, seek to the beginning."""
        if self._player.position() <= 5000 and self._playlist_index > 0:
            self._playlist_index -= 1
            self._player.setSource(self._playlist[self._playlist_index])
        else:
            self._player.setPosition(0)

    def next_clicked(self):
        if self._playlist_index < len(self._playlist) - 1:
            self._playlist += 1
            self._player.setSource(self._playlist[self._playlist_index])

    def update_buttons(self, state):
        media_count = len(self._playlist)
        self._play_action.setEnabled(
            media_count > 0 and state != QMediaPlayer.PlaybackState.PlayingState
        )
        self._pause_action.setEnabled(state == QMediaPlayer.PlaybackState.PlayingState)
        self._stop_action.setEnabled(state != QMediaPlayer.PlaybackState.StoppedState)
        self._previous_action.setEnabled(self._player.position() > 0)
        self._next_action.setEnabled(media_count > 1)

        if media_count > 0:
            file: QUrl = self._playlist[self._playlist_index]
            file_name = file.fileName()
            self.setWindowTitle(file_name)

    def show_status_message(self, message):
        self.statusBar().showMessage(message, 5000)

    def _player_error(self, error, error_string):
        print(error_string, file=sys.stderr)
        self.show_status_message(error_string)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    available_geometry = main_window.screen().availableGeometry()
    main_window.resize(int(available_geometry.width() / 3), int(available_geometry.height() / 2))

    main_window.show()
    sys.exit(app.exec())
