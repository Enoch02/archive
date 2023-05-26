package com.enoch02.dependencyinjection

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.enoch02.dependencyinjection.domain.MyRepository
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class MyViewModel @Inject constructor(private val repository: MyRepository) : ViewModel() {
    init {
        viewModelScope.launch {
            repository.doNetworkCall()
        }
    }
}