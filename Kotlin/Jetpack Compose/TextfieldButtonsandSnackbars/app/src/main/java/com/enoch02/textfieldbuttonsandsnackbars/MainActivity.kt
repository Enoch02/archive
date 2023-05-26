package com.enoch02.textfieldbuttonsandsnackbars

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material.*
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import kotlinx.coroutines.launch

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            // Remembers the scaffold state.
            val scaffoldState = rememberScaffoldState()
            // Remembers the value of the textfield.
            val textFieldState = remember{
                mutableStateOf("")
            }
            // Creates a coroutine scope.
            val scope = rememberCoroutineScope()
            Scaffold(
                modifier = Modifier.fillMaxSize(),
                scaffoldState = scaffoldState
            ) {
                Column(horizontalAlignment = Alignment.CenterHorizontally,
                verticalArrangement = Arrangement.Center,
                modifier = Modifier
                    .fillMaxSize()
                    .padding(horizontal = 30.dp)) {

                    TextField(
                        value = textFieldState.value, // Default value of the textfield
                        onValueChange = {
                            // New value of the textfield when the user enters something.
                            textFieldState.value = it
                        },
                        label = {
                            // Hint for the textfield.
                            Text(text = "Enter your name")
                        },
                        singleLine = true, // Makes the input field single line.
                        modifier = Modifier.fillMaxWidth())

                    Spacer(modifier = Modifier.height(16.dp)) // Creates a gap between widgets.

                    Button(
                        onClick = {
                            scope.launch {
                                // Shows a snackbar when the button is clicked.
                                scaffoldState.snackbarHostState.showSnackbar(
                                    message = "Hello ${textFieldState.value}",
                                    duration = SnackbarDuration.Short)
                            }
                        }) {
                        // The button text.
                        Text(text = "Please Greet Me")
                    }
                }
            }
        }
    }
}