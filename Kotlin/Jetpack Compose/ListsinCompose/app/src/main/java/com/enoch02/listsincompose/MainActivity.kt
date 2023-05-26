package com.enoch02.listsincompose

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.ScrollState
import androidx.compose.foundation.gestures.scrollable
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.itemsIndexed
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.Text
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            // Creating a list with column.
            //val scrollState = rememberScrollState()
            //Column(modifier = Modifier.verticalScroll(state = ScrollState(scrollState.value))){
            //    for (i in 1..50){
            //        Text(
            //            text = "Item $i",
            //            textAlign = TextAlign.Center,
            //            fontSize = 24.sp,
            //            fontWeight = FontWeight.Bold,
            //            modifier = Modifier
            //                .fillMaxWidth()
            //                .padding(vertical = 24.dp)
            //        )
            //    }
            //}
            // Lazy column only creates list items when they are being scrolled to.
            LazyColumn{
                items(count = 5000){
                    Text(
                        text = "Item $it",
                        fontSize = 24.sp,
                        fontWeight = FontWeight.Bold,
                        textAlign = TextAlign.Center,
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(vertical = 24.dp))
                }
            }

            // Lazily creates a list from a list... Ironic.
            //LazyColumn{
            //    itemsIndexed(listOf("This", "is", "Jetpack", "Compose")
            //    ){ index, string ->
            //        Text(
            //            text = string,
            //            fontSize = 24.sp,
            //            fontWeight = FontWeight.Bold,
            //            textAlign = TextAlign.Center,
            //            modifier = Modifier
            //                .fillMaxWidth()
            //                .padding(vertical = 24.dp))
            //        }
            //    }
            //}
        }
    }
}