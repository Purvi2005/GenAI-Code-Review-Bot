export default function IssuesList({ issues }) {
  return (
    <div className="card">
      <h2>Top Issues</h2>
      {issues.length === 0 ? (
        <p>No issues detected</p>
      ) : (
        <ul>
          {issues.map((issue, index) => (
            <li key={index}>{issue}</li>
          ))}
        </ul>
      )}
    </div>
  )
}
