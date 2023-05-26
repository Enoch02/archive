package com.enoch02.dependencyinjection

import android.app.Application
import dagger.hilt.android.HiltAndroidApp

/**
 * This class is useful for getting an instance
 * of context or Application. This class has to
 * be registered in the application manifest
 */
@HiltAndroidApp
class MyApp : Application() {

}