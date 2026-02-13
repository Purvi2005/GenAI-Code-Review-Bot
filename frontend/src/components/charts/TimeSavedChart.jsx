import { Pie } from "react-chartjs-2"
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js"

ChartJS.register(ArcElement, Tooltip, Legend)

export default function TimeSavedChart({ value }) {
  const data = {
    labels: ["Saved", "Manual"],
    datasets: [
      {
        data: [value, 100 - value],
        backgroundColor: ["#22c55e", "#e5e7eb"]
      }
    ]
  }

  return <Pie data={data} />
}
