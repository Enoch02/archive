package com.enoch2.android.datastoretest

import android.content.Context
import android.os.Bundle
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.datastore.core.DataStore
import androidx.datastore.preferences.core.Preferences
import androidx.datastore.preferences.core.edit
import androidx.datastore.preferences.core.stringPreferencesKey
import androidx.datastore.preferences.preferencesDataStore
import com.enoch2.android.datastoretest.ui.theme.DataStoreTestTheme
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map
import kotlinx.coroutines.launch


class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            DataStoreTestTheme {
                // A surface container using the 'background' color from the theme
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colors.background
                ) {
                    Scaffold(
                        topBar = { MyTopAppBar() },
                        content = { MainScreen() }
                    )
                }
            }
        }
    }
}

@Composable
fun MyTopAppBar(){
    TopAppBar(
        title = {Text(stringResource(R.string.app_name))}
    )
}

@Composable
fun MainScreen(){
    val text = remember { mutableStateOf("") }
    val result = remember { mutableStateOf("") }
    val context = LocalContext.current
    val scope = rememberCoroutineScope()
    val dataStore = StoreData(context)

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(10.dp)) {
        TextField(
            value = text.value,
            onValueChange = { text.value = it },
            modifier = Modifier.fillMaxWidth(),
            keyboardOptions = KeyboardOptions.Companion.Default)

        Spacer(modifier = Modifier.height(20.dp))

        Button(
            modifier = Modifier.fillMaxWidth(),
            onClick = {
                // Launch the class in a coroutine scope and save data.
                Toast.makeText(context, "Data saved!", Toast.LENGTH_SHORT).show()
                scope.launch {
                    dataStore.saveData(text.value)
                }
            }){
            Text("Save")
        }

        Spacer(modifier = Modifier.height(50.dp))

        val userData = dataStore.getData.collectAsState(initial = "")
        Button(onClick = { result.value = userData.value!! },
            modifier = Modifier.fillMaxWidth()) {
            Text("Load")
        }
        Text("Saved value: ${result.value}",
            modifier = Modifier.fillMaxWidth(),
            fontSize = 30.sp)
    }
}


class StoreData(private val context: Context){

    companion object{
        private val Context.dataStore: DataStore<Preferences> by preferencesDataStore("userData")
        val USER_DATA_KEY = stringPreferencesKey("user_data")
    }

    val getData: Flow<String?> = context.dataStore.data.map { preferences ->
        preferences[USER_DATA_KEY] ?: "Something" // 'Something' is the default key value.
    }

    suspend fun saveData(value: String){
        context.dataStore.edit { preferences ->
            preferences[USER_DATA_KEY] = value
        }
    }
}