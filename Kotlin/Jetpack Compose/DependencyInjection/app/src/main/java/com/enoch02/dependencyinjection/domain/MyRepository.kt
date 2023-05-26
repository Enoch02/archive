package com.enoch02.dependencyinjection.domain

interface MyRepository {
    suspend fun doNetworkCall()
}