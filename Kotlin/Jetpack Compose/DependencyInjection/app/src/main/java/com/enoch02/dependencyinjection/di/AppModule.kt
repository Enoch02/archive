package com.enoch02.dependencyinjection.di

import android.app.Application
import com.enoch02.dependencyinjection.data.remote.MyApi
import com.enoch02.dependencyinjection.domain.MyRepository
import com.enoch02.dependencyinjection.domain.MyRepositoryImpl
import dagger.Module
import dagger.Provides
import dagger.hilt.InstallIn
import dagger.hilt.components.SingletonComponent
import retrofit2.Retrofit
import javax.inject.Named
import javax.inject.Singleton

/**
 * Modules are containers for the dependencies of
 * the application. This one lasts as long as the
 * application runs.
 *
 * You can create modules for different scopes or uses
 * with different lifetimes
 */
@Module
@InstallIn(SingletonComponent::class)  // determines the lifetime of the object
object AppModule {

    /**
     * Tell DaggerHilt how to provide the dependency
     */
    @Provides
    @Singleton  // determines amount of the instances when the Interface is injected
    fun provideMyApi(): MyApi {
        return Retrofit.Builder()
            .baseUrl("https://test.com")
            .build()
            .create(MyApi::class.java)
    }

    /**
     * The api argument is supplied automatically
     * by DaggerHilt. We also do not need to call
     * any function in here manually. Ain't that neat!!
     */
    /*@Provides
    @Singleton
    fun provideMyRepository(
        api: MyApi,
        app: Application,
        @Named("hello2") hello1: String
    ): MyRepository {
        return MyRepositoryImpl(api, app)
    }*/

    /**
     * Functions with the same return type can cause compile
     * time errors. Using @Named allows us to differentiate
     * between the dependency we need to inject.
     */
    @Provides
    @Singleton
    @Named("hello1")
    fun provideString1() = "Hello 1"

    @Provides
    @Singleton
    @Named("hello2")
    fun provideString2() = "Hello 2"
}