import axios from "axios"

const API = axios.create({
  baseURL: "http://localhost:8000"
})

export const getReview = async () => {
  const res = await API.get("/latest-review")
  return res.data
}
