package com.enoch02.systembarcolorchanger

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.runtime.SideEffect
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import com.enoch02.systembarcolorchanger.ui.theme.SystemBarColorChangerTheme
import com.google.accompanist.systemuicontroller.rememberSystemUiController

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            SystemBarColorChangerTheme {
                // A surface container using the 'background' color from the theme
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background,
                    content = {
                        /*val systemUiController = rememberSystemUiController()
                        val darkTheme = isSystemInDarkTheme()

                        * Do this in Theme.kt for serious apps
                        SideEffect {
                            systemUiController.setSystemBarsColor(
                                color = if (darkTheme) Color.LightGray else Color.Blue
                            )
                        }*/
                    }
                )
            }
        }
    }
}
