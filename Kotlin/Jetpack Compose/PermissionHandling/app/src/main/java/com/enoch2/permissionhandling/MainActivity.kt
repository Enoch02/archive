package com.enoch2.permissionhandling

import android.Manifest
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material.MaterialTheme
import androidx.compose.material.Surface
import androidx.compose.material.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.DisposableEffect
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalLifecycleOwner
import androidx.compose.ui.tooling.preview.Preview
import androidx.lifecycle.Lifecycle
import androidx.lifecycle.LifecycleEventObserver
import com.enoch2.permissionhandling.ui.theme.PermissionHandlingTheme
import com.google.accompanist.permissions.ExperimentalPermissionsApi
import com.google.accompanist.permissions.rememberMultiplePermissionsState

@ExperimentalPermissionsApi
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            PermissionHandlingTheme {
                // A surface container using the 'background' color from the theme
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colors.background
                ) {
                    val permissionState = rememberMultiplePermissionsState(
                        permissions = listOf(
                            Manifest.permission.RECORD_AUDIO,
                            Manifest.permission.CAMERA
                        )
                    )

                    // Disposable effect prevents the app from asking for permission
                    // Every time it recomposes.
                    val lifeCycleOwner = LocalLifecycleOwner.current
                    DisposableEffect(key1 = lifeCycleOwner,
                        effect = {
                            val observer = LifecycleEventObserver{ _, event ->
                                if (event == Lifecycle.Event.ON_START) {
                                    permissionState.launchMultiplePermissionRequest()
                                    }
                                }
                            lifeCycleOwner.lifecycle.addObserver(observer)

                            onDispose {
                                lifeCycleOwner.lifecycle.removeObserver(observer)
                            }
                        }
                    )
                    Column(modifier = Modifier.fillMaxSize(),
                        horizontalAlignment = Alignment.CenterHorizontally,
                        verticalArrangement = Arrangement.Center) {

                        permissionState.permissions.forEach { perm ->
                            when(perm.permission){
                                Manifest.permission.CAMERA -> {
                                    when {
                                        // Checks if permission is granted.
                                        perm.hasPermission -> {
                                            Text("Camera permission accepted")
                                        }
                                        // Shows a message if permission has been rejected the 1st time
                                        perm.shouldShowRationale ->{
                                            Text("Camera permission is needed to to access" +
                                                    " the camera")
                                        }
                                        // If permission is rejected permanently / for 2nd time.
                                        perm.isPermanentlyDenied() -> {
                                            Text("Camera permission was permanently denied " +
                                                    " you can enable it in the setting")
                                        }
                                    }
                                }
                                Manifest.permission.RECORD_AUDIO -> {
                                    when {
                                        // Checks if permission is granted.
                                        perm.hasPermission -> {
                                            Text("Record audio permission accepted")
                                        }
                                        // Shows a message if permission has been rejected the 1st time
                                        perm.shouldShowRationale ->{
                                            Text("Record audio permission is needed to to access" +
                                                    " the camera")
                                        }
                                        // If permission is rejected permanently / for 2nd time.
                                        perm.isPermanentlyDenied() -> {
                                            Text("Record audio permission was permanently denied " +
                                                    " you can enable it in the setting")
                                        }
                                    }
                                }
                            }
                        }

                    }
                }
            }
        }
    }
}
