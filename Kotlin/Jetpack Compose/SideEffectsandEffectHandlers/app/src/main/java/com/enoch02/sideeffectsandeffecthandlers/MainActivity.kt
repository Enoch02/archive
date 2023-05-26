package com.enoch02.sideeffectsandeffecthandlers

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material.Button
import androidx.compose.material.Scaffold
import androidx.compose.material.Text
import androidx.compose.material.rememberScaffoldState
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import kotlinx.coroutines.launch

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            val scaffoldState = rememberScaffoldState()
            val scope = rememberCoroutineScope()
            Scaffold(scaffoldState = scaffoldState) {
                //var counter by remember {
                //    // By keyword delegates 'remember' property to counter.
                //    mutableStateOf(0)
                //}
                // produceState can create a new state and trigger a recompose.
                var counter = produceState(initialValue = 0){
                    // Asynchronous code here.
                    kotlinx.coroutines.delay(3000L)
                    value = 4
                }
                if (counter.value % 5  == 0 && counter.value > 0){
                    // When the key changes, LaunchEffect cancels the coroutine.
                    LaunchedEffect(key1 = scaffoldState.snackbarHostState) {
                        scaffoldState.snackbarHostState.showSnackbar(message = "Hello")
                    }
                }
                Button(onClick = { /*counter++*/ },
                       modifier = Modifier
                           .fillMaxWidth()
                           .padding(16.dp)
                ){
                    // The number changes to 4 after 3 seconds.
                    Text(text = "Click Me: ${counter.value}")
                }
            }
        }
    }
}