package com.enoch02.animations

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.animation.Animatable
import androidx.compose.animation.animateColorAsState
import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.animateDpAsState
import androidx.compose.animation.core.animateFloatAsState
import androidx.compose.animation.core.tween
import androidx.compose.foundation.*
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.draw.rotate
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import com.enoch02.animations.ui.theme.AnimationsTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            var currentDemo by rememberSaveable { mutableStateOf(0) }
            val max by remember { mutableStateOf(3) }

            AnimationsTheme {
                Column(
                    modifier = Modifier.fillMaxSize(),
                    verticalArrangement = Arrangement.SpaceBetween,
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    when (currentDemo) {
                        0 -> {
                            AnimatableSample(
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .fillMaxHeight(0.7f)
                            )
                        }

                        1 -> {
                            AnimateDpAsState(
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .fillMaxHeight(0.7f)
                            )
                        }
                        2 -> {
                            AnimateColorAsState(
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .fillMaxHeight(0.7f)
                            )
                        }
                        3 -> {
                            AnimateAsFloatContent(
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .fillMaxHeight(0.7f)
                            )
                        }
                        else -> {
                            currentDemo = 0
                        }
                    }

                    Column {
                        Slider(
                            value = currentDemo.toFloat(),
                            onValueChange = { currentDemo = it.toInt() },
                            modifier = Modifier.fillMaxWidth(),
                            valueRange = 0f..max.toFloat(),
                            steps = 1
                        )
                        Button(
                            onClick = { currentDemo++ },
                            content = { Text(text = "Next Demo") },
                            modifier = Modifier.fillMaxWidth()
                        )
                    }
                }
            }
        }
    }
}

@Composable
fun AnimatableSample(modifier: Modifier) {
    var isAnimated by remember { mutableStateOf(false) }
    val color = remember { Animatable(Color.DarkGray) }

    // animate to green/red based on button click
    /**
     * LaunchedEffect should be used when you want
     * that some action must be taken when composable
     * is first launched.
     */
    LaunchedEffect(isAnimated) {
        color.animateTo(
            if (isAnimated) Color.Green else Color.Red,
            animationSpec = tween(2000)
        )
    }

    Box(
        modifier = modifier.background(color.value)
    ) {
        Text(text = "Animatable API for animating a single value")
    }
    Button(
        onClick = { isAnimated = !isAnimated },
        content = {
            Text(text = "Animate Color")
        }
    )
}

@Composable
fun CircleImage(imageSize: Dp) {
    Image(
        painter = painterResource(id = R.drawable.ic_launcher_foreground),
        contentDescription = "Circle Image",
        contentScale = ContentScale.Crop,
        modifier = Modifier
            .size(imageSize)
            .clip(CircleShape)
            .border(5.dp, Color.Gray, CircleShape)
    )
}

@Composable
fun AnimateDpAsState(modifier: Modifier) {
    val isNeedExpansion = rememberSaveable { mutableStateOf(false) }

    val animatedSizeDp: Dp by animateDpAsState(targetValue = if (isNeedExpansion.value) 350.dp else 100.dp)

    Column(
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally,
        modifier = modifier
    ) {
        CircleImage(imageSize = animatedSizeDp)
        Button(
            onClick = { isNeedExpansion.value = !isNeedExpansion.value },
            modifier = Modifier
                .padding(top = 50.dp)
                .width(300.dp),
            content = {
                Text(text = "animateDpAsState")
            }
        )
    }
}

@Composable
fun AnimateColorAsState(modifier: Modifier) {
    var isNeedColorChange by remember { mutableStateOf(false) }
    val startColor = Color.Blue
    val endColor = Color.Green
    val backgroundColor by animateColorAsState(
        targetValue = if (isNeedColorChange) endColor else startColor,
        animationSpec = tween(
            durationMillis = 2000,
            delayMillis = 100,
            easing = LinearEasing
        )
    )

    Column {
        Box(modifier = modifier.background(backgroundColor))
        Button(
            onClick = { isNeedColorChange = !isNeedColorChange },
            modifier = Modifier.padding(top = 10.dp),
            content = {
                Text(text = "Switch Color")
            }
        )
    }
}

@Composable
fun AnimateAsFloatContent(modifier: Modifier) {
    var isRotated by rememberSaveable { mutableStateOf(false) }
    val rotationAngle by animateFloatAsState(
        targetValue = if (isRotated) 360f else 0f,
        animationSpec = tween(durationMillis = 2500)
    )

    Column(
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally,
        modifier = modifier
    ) {
        Image(
            painter = painterResource(R.drawable.fan),
            contentDescription = "fan",
            modifier = Modifier
                .rotate(rotationAngle)
                .size(150.dp)
        )

        Button(
            onClick = { isRotated = !isRotated },
            modifier = Modifier
                .padding(top = 50.dp)
                .width(200.dp),
            content = {
                Text(text = "Rotate Fan")
            }
        )
    }
}