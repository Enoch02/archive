package com.enoch02.hellocompose

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.material.Text
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color

class MainActivity : ComponentActivity() {
    // Called when the activity is created.
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // Assigns composable functions to MainActivity.
        setContent {
            // Displays items vertically.
            Column(
                modifier = Modifier
                    // Height and width of the widget can be manually set.
                    //.width(100.dp)
                    //.height(500.dp)
                    //.fillMaxHeight() // Fill maximum height available.
                    //.fillMaxWidth() // Fill maximum width available.
                    .fillMaxSize() // Allows to column to fit the entire screen.
                    .background(Color.Green), // Sets the background as green.
                horizontalAlignment = Alignment.CenterHorizontally, // Centers the widgets in Column
                verticalArrangement = Arrangement.Center,
            ) {
                Text(text = "Hello World")
                Text(text = "Hello Again")
            }
        }
    }
}