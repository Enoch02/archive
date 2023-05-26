package com.enoch02.stylingtextcompose

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.material.Text
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.SpanStyle
import androidx.compose.ui.text.buildAnnotatedString
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.text.style.TextDecoration
import androidx.compose.ui.text.withStyle
import androidx.compose.ui.unit.sp

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            Column(
                modifier = Modifier
                    .fillMaxWidth()
                    .fillMaxHeight(),
                verticalArrangement = Arrangement.SpaceEvenly,
                horizontalAlignment = Alignment.CenterHorizontally
            ){
                Box(
                    modifier = Modifier
                        .background(Color.Red)
                ) {
                    Text(
                        text = "Jetpack Compose",
                        color = Color.White,
                        fontSize = 30.sp, textAlign = TextAlign.Center,
                        textDecoration = TextDecoration.Underline,
                    )
                }

                Box(
                    modifier = Modifier.background(Color.Yellow)
                ){
                Text(
                    // Allows styling of specific parts of a string.
                    text = buildAnnotatedString {
                        withStyle(
                            SpanStyle(
                                color = Color.Green,
                                fontSize = 50.sp,
                            )
                        ){
                            append("J")
                        }
                        append("etpack ")

                        withStyle(
                            SpanStyle(
                                color = Color.Green,
                                fontSize = 50.sp,
                            )
                        ){
                            append("C")
                        }
                        append("ompose")
                    },
                    color = Color.Black,
                    fontSize = 30.sp, textAlign = TextAlign.Center,
                    textDecoration = TextDecoration.None,)
                }
            }
        }
    }
}