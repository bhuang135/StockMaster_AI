# 📈 StockMaster AI
## AI-Powered Investment Research & RAG Chat System

StockMaster AI is a multilingual Streamlit financial intelligence platform. It supports **繁體中文 / 简体中文 / English** in the app interface, AI investment report, chatbot response, and downloadable DOCX report.

---

## Core Features

- Built-in language switcher: Traditional Chinese, Simplified Chinese, English
- Financial data retrieval from Yahoo Finance through `yfinance`
- 5-year historical stock price chart with moving averages
- Key fundamentals and financial statement summary
- News sentiment scoring and scenario valuation
- Gemini AI institutional investment report
- RAG chatbot with source-aware responses
- DOCX report export in the selected app language

---

## Main App File

```text
stock_master_streamlit.py
```

Deploy this file as the Streamlit entry point.

---

## Project Structure

```text
StockMaster_AI/
├── stock_master_streamlit.py       # Streamlit frontend and app controller
├── stock_data_utils_fixed.py       # Data, valuation, Gemini, report generation
├── rag_chat_pipeline.py            # RAG chatbot retrieval and answer generation
├── translations.py                 # Built-in trilingual UI / prompt dictionary
├── requirements.txt                # Python dependencies
├── .streamlit/config.toml          # Streamlit cloud config
├── GITHUB_DEPLOY.md                # GitHub + Streamlit deployment guide
├── SETUP.md                        # Local setup guide
├── USER_GUIDE.md                   # User workflow guide
└── ARCHITECTURE.md                 # System architecture notes
```

---

## Run Locally

```bash
pip install -r requirements.txt
streamlit run stock_master_streamlit.py
```

Open:

```text
http://localhost:8501
```

---

## API Key Handling

Gemini API Key is entered by the user in the sidebar. It is only stored in the current browser session and is not written to disk, code, or GitHub.

---

## Deployment

Use Streamlit Community Cloud and set:

```text
Main file path: stock_master_streamlit.py
Python version: 3.12+
```

See `GITHUB_DEPLOY.md` for the full workflow.
