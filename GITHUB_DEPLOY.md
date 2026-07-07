# StockMaster AI — GitHub / Streamlit Deployment Guide

This project is a **Streamlit Python app**. GitHub stores the code; Streamlit Community Cloud runs the app from your GitHub repo.

---

## 1. Local Test Before Push

```bash
cd StockMaster_AI
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run app:

```bash
streamlit run stock_master_streamlit.py
```

Open:

```text
http://localhost:8501
```

---

## 2. Push Updated Files to GitHub

If your repo already exists and `origin` is already configured:

```bash
cd C:\Users\Desktop\Git_StockMaster\StockMaster_AI
git status
git add .
git commit -m "Add multilingual language switcher"
git push
```

If the remote URL is still the placeholder, fix it first:

```bash
git remote set-url origin https://github.com/bhuang135/StockMaster_AI.git
git remote -v
git push -u origin main
```

---

## 3. Streamlit Community Cloud Settings

Use these settings:

```text
Repository: bhuang135/StockMaster_AI
Branch: main
Main file path: stock_master_streamlit.py
Python version: 3.12+
```

---

## 4. Multilingual Behavior

The app supports:

```text
繁體中文
简体中文
English
```

The selected language controls:

- UI labels
- Tabs
- Metric names
- Financial metric guide
- Gemini AI investment report
- RAG chatbot answer
- DOCX report export

The translation dictionary is stored in:

```text
translations.py
```

---

## 5. API Key Handling

Do **not** commit any API key to GitHub.

Gemini API Key is entered in the sidebar and stored only in the current browser session.
