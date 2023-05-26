package com.enoch02.retrofitdemo.data

import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.launch

class MainViewModel : ViewModel() {
    var movieListResponse: List<Movie> by mutableStateOf(listOf())
    var errorMessage by mutableStateOf("")

    fun getMovieList(): List<Movie> {
        viewModelScope.launch {
            try {
                val apiService = ApiService.getInstance()
                movieListResponse = apiService.getMovies()
            } catch (e: Exception) {
                errorMessage = e.message.toString()
            }
        }
        return movieListResponse
    }
}