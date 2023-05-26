package com.enoch02.yacc

import android.content.Context
import android.content.Intent
import android.net.Uri
import androidx.compose.foundation.Image
import androidx.compose.foundation.clickable
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.material.*
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.style.TextAlign
import com.enoch02.yacc.router.Screen
import com.enoch02.yacc.router.BackButtonHandler
import com.enoch02.yacc.router.Router

@Composable
fun AboutActivity(){
    BackButtonHandler {
        Router.navigateTo(Screen.MainScreen)
    }

    Scaffold(
        topBar = {
            TopAppBar(title = { Text(text = "YACC") },
                navigationIcon = {
                    IconButton(onClick = { Router.navigateTo(Screen.MainScreen) }) {
                        Icon(Icons.Filled.ArrowBack, "backIcon")
                    }
                }
            )
        },
        content = { AboutMe() }
    )
}

@Composable
fun AboutMe(){
    val darkTheme = isSystemInDarkTheme()
    val textColor = if (darkTheme) { Color.White } else { Color.Black }
    val githubImage = if (darkTheme){ R.drawable.github_logo_white } else { R.drawable.github_logo }
    val context: Context = LocalContext.current
    val intent = remember {
        Intent(Intent.ACTION_VIEW, Uri.parse("https://github.com/Enoch02"))
    }
    val lines = listOf(R.string.line1, R.string.line2)

    Column(
        modifier = Modifier.fillMaxSize(),
        verticalArrangement = Arrangement.Bottom,
        horizontalAlignment = Alignment.CenterHorizontally){
        lines.forEach { line ->
            CreateText(
                text = stringResource(line),
                modifier = Modifier
                    .fillMaxWidth(), fontSize = 40, textAlign = TextAlign.Center, color = textColor)
        }
        Image(
            painter = painterResource(id = githubImage),
            contentDescription = null,
            contentScale = ContentScale.Fit,
            modifier = Modifier
                .fillMaxWidth()
                .clickable { context.startActivity(intent) }
        )
    }
}
