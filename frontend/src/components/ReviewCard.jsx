export default function ReviewCard({ repo, summary }) {
  return (
    <div className="card">
      <h2>Repository</h2>
      <p>{repo}</p>

      <h2>AI Review Summary</h2>
      <p>{summary}</p>
    </div>
  )
}
