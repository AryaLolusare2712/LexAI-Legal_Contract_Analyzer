# ⚖️ LexAI — Legal Contract Analyzer

<div align="center">

**AI-powered contract intelligence that detects legal risks, flags unfair clauses, and benchmarks agreements against industry standards.**

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Streamlit-FF4B4B?style=for-the-badge)](https://lexai-legalcontractanalyzer-u3jyuhvkz2xhzg4uqfjc69.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Gemini](https://img.shields.io/badge/Gemini_2.5_Flash-Google_AI-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## 🧠 What is LexAI?

LexAI is an intelligent legal contract analysis tool that uses **Google Gemini 2.5 Flash** to automatically review and evaluate legal agreements. Instead of spending hours (or thousands of dollars) on legal reviews, LexAI transforms raw contract text into clear, structured risk reports in seconds.

It supports NDAs, Employment Contracts, SaaS Terms, Partnership Agreements, Vendor Contracts, and Lease Agreements — and gives you:

- 🔴 **Flagged risky clauses** with excerpts and suggested rewrites
- 📊 **Industry benchmarking** to see how your contract stacks up
- 📄 **Clause coverage analysis** to catch missing legal protections
- 🎯 **A 0–100 risk score** with an interactive visual indicator

> ⚠️ **Disclaimer:** LexAI is an AI-assisted tool meant to help you understand contracts faster. It is **not a substitute for professional legal advice**. Always consult a qualified attorney before signing legally binding agreements.

---

## ✨ Features

### 🔍 AI-Powered Contract Analysis
Paste any legal document and get structured JSON insights extracted via low-temperature LLM inference — ensuring consistent, reliable output every time.

### ⚠️ Risk Detection System
Every problematic clause is classified by severity:
- 🔴 **High** — Clauses that could expose you to major legal or financial liability
- 🟡 **Medium** — Terms that deviate from fair practice and warrant negotiation
- 🟢 **Low** — Minor concerns worth noting but not immediately alarming

Each flag includes the exact problematic excerpt, an explanation of the legal issue, the business impact, and a concrete suggested revision.

### 📊 Industry Benchmarking
LexAI compares your contract's terms against market standards for its contract type, flagging deviations as:
- ✅ **OK** — Aligns with standard practice
- ⚠️ **Warning** — Deviates from norms, review recommended
- ❌ **Critical** — Significantly below acceptable standards

### 📄 Clause Coverage Analysis
Detects the presence or absence of essential legal clauses. Missing a termination clause? No dispute resolution mechanism? LexAI will catch it.

### 🎯 Risk Score Visualization
Generates an overall **0–100 risk score** rendered as an interactive SVG ring indicator — color-coded green to red based on severity.

### 🎨 Professional Dark UI
A custom-styled Streamlit interface with DM Serif + DM Sans typography, a dark `#0f0f13` background, and a multi-tab insights dashboard.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | Streamlit 1.35+ |
| **AI Model** | Google Gemini 2.5 Flash |
| **AI SDK** | `google-generativeai` |
| **Data Processing** | Pandas |
| **Styling** | Custom CSS (injected via `st.markdown`) |
| **Language** | Python 3.9+ |

---

## 🏗️ Architecture

```
User Input (Contract Text)
        │
        ▼
  ┌─────────────────┐
  │  Streamlit UI   │  ← Dark-themed, multi-tab dashboard
  └────────┬────────┘
           │
           ▼
  ┌─────────────────────────────────────┐
  │  analyze_contract()                 │
  │  • Configures Gemini client         │
  │  • Sends structured JSON prompt     │
  │  • temperature=0.2 for consistency  │
  │  • response_mime_type="application/json" │
  └────────────────┬────────────────────┘
                   │
                   ▼
        ┌──────────────────┐
        │ Gemini 2.5 Flash │  ← Google AI API
        └────────┬─────────┘
                 │ JSON Response
                 ▼
  ┌──────────────────────────────┐
  │  Parsed Result               │
  │  ├── riskScore (0–100)       │
  │  ├── summary (2-sentence)    │
  │  ├── flags[] (4–7 items)     │
  │  ├── comparison[] (6–8 rows) │
  │  └── clauses[] (6–10 items)  │
  └──────────────────────────────┘
           │
           ▼
  ┌────────────────────────────┐
  │  3-Tab Results Dashboard   │
  │  ├── ⚠️ Risk Flags         │
  │  ├── 📊 Template Comparison│
  │  └── 📄 All Clauses        │
  └────────────────────────────┘
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- A [Google AI API key](https://aistudio.google.com/app/apikey) (free tier available)

### 1. Clone the Repository

```bash
git clone https://github.com/AryaLolusare2712/LexAI-Legal_Contract_Analyzer.git
cd LexAI-Legal_Contract_Analyzer
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`.

### 4. Analyze a Contract

1. Enter your **Google AI API key** in the sidebar
2. Select the **contract type** (NDA, Employment, SaaS, etc.)
3. Paste your contract text — or click **"Load Sample NDA"** to try a demo
4. Click **⚖️ Analyze Contract** and review your results across three tabs

---

## 📦 Dependencies

```
streamlit>=1.35.0
google-generativeai>=0.8.0
pandas>=2.0.0
```

---

## 📁 Project Structure

```
LexAI-Legal_Contract_Analyzer/
├── app.py              # Main Streamlit application (single-file architecture)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 🔮 Roadmap / Future Enhancements

The sidebar notes a planned production-grade stack:

- [ ] **LangChain chains** for multi-step legal reasoning
- [ ] **RAG over a legal clause vector store** — compare against a database of thousands of real clauses
- [ ] **FAISS / Pinecone vector index** for semantic clause retrieval
- [ ] PDF / DOCX upload support (beyond plain text input)
- [ ] Export reports as PDF
- [ ] Clause redlining with suggested tracked changes

---

## 🤝 Contributing

Contributions are welcome! To get started:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Arya Lolusare**
- GitHub: [@AryaLolusare2712](https://github.com/AryaLolusare2712)

---

<div align="center">

Made with ⚖️ and AI · Not a substitute for real legal advice

</div>
