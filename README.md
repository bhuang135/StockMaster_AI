# 📈 StockMaster AI  
## AI-Powered Investment Research & RAG Chat System

StockMaster AI is an AI-driven financial intelligence platform that integrates:

- Financial data retrieval
- News sentiment analysis
- Scenario valuation
- Retrieval-Augmented Generation (RAG) chatbot
- Interactive Streamlit dashboard

This system demonstrates an end-to-end AI investment analysis workflow designed for structured decision support and financial insight generation.

---

# 🚀 Project Overview

Modern investors face three major challenges:

1. Too much fragmented financial information  
2. Limited structured insights  
3. Lack of explainable decision support  

StockMaster AI solves this by combining:

Market Data + Sentiment + Simulation + AI Reasoning

Into a single unified platform.

---

# 🎯 Core Features

## 📊 Financial Data Retrieval

Automatically retrieves:

- Company fundamentals
- Historical price data
- Key financial metrics
- Financial statements

Sources:

Yahoo Finance API  
Public financial datasets

---

## 📰 News Sentiment Analysis

The system evaluates recent news and produces:

Positive / Neutral / Negative sentiment

Score range:

-0.15 to +0.15

Used in:

- Valuation modeling
- AI reasoning

---

## 📈 Scenario Valuation Engine

Simulates:

Positive Scenario (Bull)  
Neutral Scenario (Base)  
Negative Scenario (Bear)

Used to evaluate:

Forward price expectations  
Risk-adjusted projections

---

## 🤖 RAG Chatbot

Supports intelligent financial Q&A such as:

Who is the CEO of AAPL?  
What products does NVDA sell?  
Explain Tesla revenue trend  
What caused recent price movement?

Pipeline:

User Question → Query Expansion → Retrieval → Ranking → LLM Response

Technologies:

TF-IDF  
Cosine Similarity  
Gemini LLM

---

# 🧩 Project Structure

StockMaster_AI/

stock_master_streamlit.py  
stock_data_utils_fixed.py  
rag_chat_pipeline.py  
run_dashboard.bat  
requirements.txt  

README.md  
ARCHITECTURE.md  
SETUP.md  
USER_GUIDE.md  

---

# 🛠 Technology Stack

Frontend:

Streamlit  
Plotly  

Backend:

Python  
Pandas  
NumPy  

AI:

Gemini LLM  
TF-IDF Retrieval  
Cosine Similarity  

---

# 📌 Summary

StockMaster AI represents an:

End-to-End AI Financial Intelligence System

Combining:

Data + Analytics + AI + Visualization