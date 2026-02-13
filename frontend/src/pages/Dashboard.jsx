import { useEffect, useState } from "react"
import { getReview } from "../services/api"
import ReviewCard from "../components/ReviewCard"
import IssuesList from "../components/IssuesList"
import TimeSavedChart from "../components/charts/TimeSavedChart"
import IssuesChart from "../components/charts/IssuesChart"

export default function Dashboard() {
  const [data, setData] = useState(null)

  useEffect(() => {
    getReview().then(setData)
  }, [])

  if (!data) return <h2 style={{ padding: "20px" }}>Loading...</h2>

  return (
    <div style={{ padding: "30px" }}>
      <h1>GenAI Code Review Dashboard</h1>
      <span className="badge">Live AI Review</span>

      <div className="grid" style={{ marginTop: "20px" }}>
        <ReviewCard repo={data.repo} summary={data.summary} />
        <IssuesList issues={data.issues} />
      </div>

      <div className="grid" style={{ marginTop: "20px" }}>
        <div className="card">
          <h2>Review Time Saved</h2>
          <TimeSavedChart value={data.time_saved} />
        </div>

        <div className="card">
          <h2>Issue Distribution</h2>
          <IssuesChart issues={data.issues} />
        </div>
      </div>
    </div>
  )
}
