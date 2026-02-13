import { Bar } from "react-chartjs-2"
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Tooltip, Legend } from "chart.js"

ChartJS.register(CategoryScale, LinearScale, BarElement, Tooltip, Legend)

export default function IssuesChart({ issues }) {
  const data = {
    labels: issues,
    datasets: [
      {
        label: "Issue Count",
        data: issues.map(() => 1),
        backgroundColor: "#3b82f6"
      }
    ]
  }

  return <Bar data={data} />
}
