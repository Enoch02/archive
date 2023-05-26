package com.enoch02.composemodifiers

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.material.Text
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp


class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            Column(
                modifier = Modifier
                    .background(Color.Green)
                    .fillMaxHeight(0.5f) // Sets max height to 50% of the screen.
                    .fillMaxWidth()
                    //.padding(top = 50.dp) // Push contents of a container in different directions.
                    .border(5.dp, Color.Magenta) // Creates a border with rectangular shape.
                    // .requiredWidth(300.dp) // Overrides normal width.
                    .padding(5.dp)
                    .border(5.dp, Color.Blue)
                    .padding(5.dp)
                    .border(10.dp, Color.Red)
                    .padding(10.dp)
            ) {
                Text(text = "Hello", modifier = Modifier
                    .clickable {
                        // The code here is called when the widget is clicked.
                    }
                    // It starts from the top left corner (0, 0).
                    //.offset(20.dp, 20.dp) // Offset/move the widget without moving other widget.
                )
                // Creates an empty composable with height 50dp.
                Spacer(modifier = Modifier
                    .height(50.dp))
                Text(text = "World")
            }
        }
    }
}