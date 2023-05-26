package com.enoch02.dependencyinjection.di

import com.enoch02.dependencyinjection.domain.MyRepository
import com.enoch02.dependencyinjection.domain.MyRepositoryImpl
import dagger.Binds
import dagger.Module
import dagger.hilt.InstallIn
import dagger.hilt.components.SingletonComponent
import javax.inject.Singleton

/**
 * Another method for providing a dependency.
 * This method is for injecting interfaces and abstract
 * classes.
 */
@Module
@InstallIn(SingletonComponent::class)
abstract class RepositoryModule {

    @Binds
    @Singleton
    abstract fun bindMyRepository(myRepositoryImpl: MyRepositoryImpl): MyRepository
}