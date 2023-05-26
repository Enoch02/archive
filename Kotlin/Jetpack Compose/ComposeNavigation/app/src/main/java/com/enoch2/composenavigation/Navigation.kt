package com.enoch2.composenavigation

import androidx.compose.foundation.layout.*
import androidx.compose.material.Button
import androidx.compose.material.Text
import androidx.compose.material.TextField
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import androidx.navigation.NavType
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.navArgument
import androidx.navigation.compose.rememberNavController

@Composable
fun Navigation() {
    val navController = rememberNavController()
    // first screen that shows
    NavHost(navController = navController, startDestination = Screen.MainScreen.route) {
        // tell the nav host about our Screens
        composable(route = Screen.MainScreen.route) {
            // specify the composable that the route represents
            MainScreen(navController = navController)
        }

        composable(
            // append the argument to the route
            // use ?name={name} for optional args
            route = Screen.DetailScreen.route + "/{name}", // you can add multiple args like this: /{name}/{age}
            // list of arguments for the composable
            arguments = listOf(
                navArgument("name") {
                    // sets constraints for the argument
                    type = NavType.StringType
                    defaultValue = "Enoch"
                    nullable = true
                }
            )
        ) { entry ->
            // gets the value of our argument
            DetailScreen(name = entry.arguments?.getString("name"))
        }
    }
}

@Composable
fun MainScreen(navController: NavController) {
    var text by remember { mutableStateOf("") }
    Column(
        verticalArrangement = Arrangement.Center,
        modifier = Modifier
            .fillMaxSize()
            .padding(horizontal = 50.dp)
    ) {
        TextField(
            value = text,
            onValueChange = { text = it },
            modifier = Modifier.fillMaxWidth()
        )
        Spacer(modifier = Modifier.height(8.dp))
        Button(
            onClick = {
                // navigate to a specific path with args built by the function
                navController.navigate(Screen.DetailScreen.withArgs(text))
            },
            modifier = Modifier.align(Alignment.End)
        ) {
            Text(text = "To DetailScreen")
        }
    }
}

@Composable
fun DetailScreen(name: String?) {
    Box(
        contentAlignment = Alignment.Center,
        modifier = Modifier.fillMaxSize()
    ) {
        Text(text = "Hello, $name")
    }
}
