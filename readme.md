# 🚀 GenAI Automated Code Review System

An AI-powered automated code review system that integrates with GitHub pull requests to provide **intelligent, prioritized, and context-aware code reviews**, reducing manual review time by up to **70%**.

The system uses **Gemini AI**, a **multi-agent analysis pipeline**, and a **ScaleDown engine** to handle large pull requests efficiently and present results through a **live React dashboard**.

---

## ✨ Key Features

- 🔍 **Automated GitHub Pull Request Review**
- 🧠 **GenAI-powered reasoning using Gemini**
- 🧩 **Multi-Agent Architecture**
  - Security Scanner
  - Style & Performance Analyzer
  - Feedback Ranker
- 📉 **ScaleDown Engine**
  - Compresses large PR diffs by ~80%
  - Preserves logic and intent
- 🛡️ **Security Vulnerability Detection**
- ⚡ **Performance & Code Style Suggestions**
- 📝 **Concise PR Summarization**
- 💬 **Automatic GitHub PR Comments**
- 📊 **Live Review Dashboard (React)**
- ⏱️ **Review Time Reduction Metrics**

---

## 🏗️ System Architecture

GitHub Pull Request
↓
Webhook Trigger
↓
Fetch PR Diff
↓
ScaleDown Engine
↓
┌───────────────┬────────────────┬──────────────────┐
│ Security Agent│ Style Agent │ Performance Agent │
└───────────────┴────────────────┴──────────────────┘
↓
Feedback Ranker (GenAI)
↓
Final AI Review
↓
┌───────────────┬────────────────┐
│ GitHub Comment│ React Dashboard│
└───────────────┴────────────────┘

---

## 🛠️ Tech Stack

### Backend
- **Python**
- **FastAPI**
- **Gemini AI (google-genai SDK)**
- GitHub REST API

### Frontend
- **React + JavaScript**
- **Vite**
- **Chart.js**
- Axios

---

## 📂 Project Structure

genai-code-review-bot/
│
├── backend/
│ ├── app/
│ │ ├── ai/
│ │ ├── github/
│ │ ├── scaledown/
│ │ ├── security/
│ │ ├── style/
│ │ ├── ranker/
│ │ └── services/
│ └── .env
│
├── frontend/
│ ├── src/
│ │ ├── components/
│ │ ├── pages/
│ │ ├── services/
│ │ └── components/charts/
│
└── README.md

---

## ⚙️ Environment Variables

Create a `.env` file inside `backend/`:

```env
GEMINI_API_KEY=your_gemini_api_key
GITHUB_TOKEN=your_github_personal_access_token
-----


Commands to Execute the Program:
Backend:
1. Navigate to the backend directory:
2. Install dependencies:
   pip install -r requirements.txt
3. Run the FastAPI server:
   uvicorn app.main:app --reload

Frontend:
1. Navigate to the frontend directory:
2. Install dependencies:
   npm install
3. Start the React development server:
   npm run dev  
   ----
The free version of Gemini API has a limit of 1000 tokens per request, which may not be sufficient for large pull requests. 
To handle this, the system uses a ScaleDown engine that compresses the PR diff while preserving its logic and intent, 
allowing it to fit within the token limit and still provide meaningful reviews.If the limit has beem reached the system will be notifies that the limit has been reached and the review will be skipped.