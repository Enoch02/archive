package com.enoch02.dependencyinjection

import android.app.Service
import android.content.Intent
import android.os.IBinder
import com.enoch02.dependencyinjection.domain.MyRepository
import dagger.hilt.android.AndroidEntryPoint
import kotlinx.coroutines.runBlocking
import javax.inject.Inject

@AndroidEntryPoint // for android components
class MyService : Service() {
    /**
     * Field injection... for classes that
     * can not have a constructor.
     */
    @Inject
    lateinit var repository: MyRepository

    override fun onCreate() {
        super.onCreate()
        runBlocking {
            repository.doNetworkCall()
        }
    }

    override fun onBind(intent: Intent?): IBinder? {
        return null
    }
}