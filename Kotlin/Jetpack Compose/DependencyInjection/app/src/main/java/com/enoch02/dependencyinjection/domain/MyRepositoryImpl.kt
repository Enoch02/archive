package com.enoch02.dependencyinjection.domain

import android.app.Application
import com.enoch02.dependencyinjection.R
import com.enoch02.dependencyinjection.data.remote.MyApi
import javax.inject.Inject

class MyRepositoryImpl @Inject constructor(
    private val api: MyApi,
    private val context: Application
) : MyRepository {
    init {
        val appName = context.getString(R.string.app_name)
        println("Hello from the repository. The app name is $appName")
    }

    override suspend fun doNetworkCall() {
        println("Doing a network call")
    }
}