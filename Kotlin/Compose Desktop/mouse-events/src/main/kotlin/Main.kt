// Copyright 2000-2021 JetBrains s.r.o. and contributors. Use of this source code is governed by the Apache 2.0 license that can be found in the LICENSE file.
import androidx.compose.desktop.DesktopMaterialTheme
import androidx.compose.desktop.ui.tooling.preview.Preview
import androidx.compose.foundation.ExperimentalFoundationApi
import androidx.compose.foundation.background
import androidx.compose.foundation.combinedClickable
import androidx.compose.foundation.layout.*
import androidx.compose.material.Button
import androidx.compose.material.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.input.pointer.pointerMoveFilter
import androidx.compose.ui.text.font.FontStyle
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.compose.ui.window.Window
import androidx.compose.ui.window.application

@OptIn(ExperimentalFoundationApi::class)
@Composable
@Preview
fun ClickListenerDemo() {
    var count by remember { mutableStateOf(0) }
    Box(
        modifier = Modifier.fillMaxWidth(),
        contentAlignment = Alignment.Center
    ) {
        var text by remember { mutableStateOf("Click magenta box!") }

        Column {
            Box(
                modifier = Modifier
                    .background(Color.Magenta)
                    .fillMaxWidth(0.7f)
                    .fillMaxHeight(0.2f)
                    .combinedClickable(
                        onClick = {
                            text = "Click! ${count++}"
                        },
                        onDoubleClick = {
                            text = "Double click! ${count++}"
                        },
                        onLongClick = {
                            text = "Long click! ${count++}"
                        }
                    )
            )
            Text(text = text, fontSize = 40.sp)
        }
    }
}

@Composable
fun MouseMoveListenerDemo() {
    var color by remember { mutableStateOf(Color(0, 0, 0)) }

    Box(
        modifier = Modifier
            .wrapContentSize(Alignment.Center)
            .fillMaxWidth()
            .heightIn(300.dp)
            .background(color = color)
            .pointerMoveFilter(onMove = {
                color = Color(it.x.toInt() % 256, it.y.toInt() % 256, (it.y * it.x).toInt() % 256)
                return@pointerMoveFilter true
            })
    ) {
        Text("Red: ${color.red}, Blue: ${color.blue}, Green: ${color.green}")
    }
}

@Composable
fun MouseEnterListeners() {
    Column(
        modifier = Modifier
            .background(Color.White)
            .padding(8.dp)
            .heightIn(300.dp),
        verticalArrangement = Arrangement.spacedBy(10.dp)
    ) {
        repeat(10) { index ->
            var active by remember { mutableStateOf(false) }
            Text(
                modifier = Modifier
                    .fillMaxWidth()
                    .background(color = if (active) Color.Green else Color.White)
                    .pointerMoveFilter(
                        onEnter = {
                            active = true
                            return@pointerMoveFilter active
                        },
                        onExit = {
                            active = false
                            return@pointerMoveFilter active
                        }
                    ),
                fontSize = 30.sp,
                fontStyle = if (active) FontStyle.Italic else FontStyle.Normal,
                text = "Item $index"
            )
        }
    }
}

fun main() = application {
    var currentDemo by remember { mutableStateOf(0) }
    Window(onCloseRequest = ::exitApplication) {
        DesktopMaterialTheme {
            Column {
                when (currentDemo) {
                    0 -> {
                        ClickListenerDemo()
                    }
                    1 -> {
                        MouseMoveListenerDemo()
                    }
                    2 -> {
                        MouseEnterListeners()
                    }
                    else -> {
                        currentDemo = 0
                    }
                }

                Button(
                    modifier = Modifier
                        .fillMaxWidth(0.5f)
                        .align(Alignment.CenterHorizontally)
                        .padding(top = 30.dp),
                    onClick = { currentDemo++ }
                ) {
                    Text("Next Demo")
                }
                Text(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(10.dp),
                    text = "Current Demo: $currentDemo",
                    textAlign = TextAlign.Center
                )
            }
        }
    }
}
