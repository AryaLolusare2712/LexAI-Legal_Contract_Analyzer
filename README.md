# ⚖️ LexAI — Legal Contract Analyzer

> AI-powered contract intelligence tool that detects legal risks, flags unfair clauses, and benchmarks agreements against industry standards.

---

## 🚀 Overview

**LexAI** is an intelligent contract analysis system that leverages **LLMs (Gemini 2.5 Flash)** to automatically evaluate legal agreements such as NDAs, employment contracts, SaaS terms, and more.

It transforms complex legal text into **structured insights**, helping users:
- Identify risky clauses  
- Understand legal implications  
- Get actionable suggestions  
- Compare contracts with market standards  

---

## ✨ Features

### 🔍 AI Contract Analysis
- Extracts key clauses from raw contract text  
- Generates structured JSON insights  
- Uses low-temperature LLM inference for consistent output  

### ⚠️ Risk Detection System
- Classifies risks into:
  - 🔴 High  
  - 🟡 Medium  
  - 🟢 Low  
- Highlights problematic excerpts with explanations  

### 📊 Smart Benchmarking
- Compares contract terms with **industry standards**  
- Flags deviations using:
  - ✅ OK  
  - ⚠️ Warning  
  - ❌ Critical  

### 📄 Clause Coverage Analysis
- Detects presence/absence of essential clauses  
- Provides descriptions for missing components  

### 🎯 Risk Score Visualization
- Generates an overall **0–100 risk score**  
- Displays an interactive circular risk indicator  

### 🎨 Modern UI (Streamlit)
- Dark-themed professional interface  
- Clean typography & structured layout  
- Multi-tab insights dashboard  

---

## 🧠 Tech Stack

| Layer        | Technology |
|-------------|------------|
| Frontend    | Streamlit |
| AI Model    | Google Gemini 2.5 Flash |
| SDK         | google-generativeai |
| Data        | Pandas |
| Styling     | Custom CSS |

---

## 🏗️ Architecture
