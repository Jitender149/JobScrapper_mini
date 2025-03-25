"use client"

import { useState } from "react"
import "./App.css"
import SearchForm from "./components/SearchForm"
import JobList from "./components/JobList"
import Header from "./components/Header"
import Footer from "./components/Footer"

function App() {
  const [jobs, setJobs] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const searchJobs = async (searchParams) => {
    setLoading(true)
    setError(null)

    try {
      // Build query string from search parameters
      const queryParams = new URLSearchParams()
      Object.entries(searchParams).forEach(([key, value]) => {
        if (value) queryParams.append(key, value)
      })

      const response = await fetch(`http://localhost:5000/api/jobs?${queryParams}`)

      if (!response.ok) {
        throw new Error(`Error: ${response.status}`)
      }

      const data = await response.json()
      setJobs(data)
    } catch (err) {
      setError(err.message)
      setJobs([])
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app">
      <Header />
      <main className="main-content">
        <SearchForm onSearch={searchJobs} />
        {error && <div className="error-message">Error: {error}</div>}
        {loading ? (
          <div className="loading">
            <div className="spinner"></div>
            <p>Searching for jobs...</p>
          </div>
        ) : (
          <JobList jobs={jobs} />
        )}
      </main>
      <Footer />
    </div>
  )
}

export default App

