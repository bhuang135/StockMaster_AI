# ⚙️ StockMaster AI Setup Guide

---

## 1. Install Python

Recommended:

```text
Python 3.12+
```

Check:

```bash
python --version
```

---

## 2. Create Virtual Environment

```bash
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

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run Application

```bash
streamlit run stock_master_streamlit.py
```

Or on Windows:

```bash
run_dashboard.bat
```

Open:

```text
http://localhost:8501
```

---

## 5. Language Switching

The app now supports:

```text
繁體中文
简体中文
English
```

The selected language controls:

- Sidebar labels
- Dashboard tabs
- Metric names
- Financial metric guide
- AI investment report language
- Chatbot answer language
- DOCX report language

The translation logic is stored in:

```text
translations.py
```

---

## 6. Gemini API Key

Gemini API Key is not hardcoded and is not stored in GitHub. Each user enters their own key in the sidebar.

The key is only cached in the browser session and is cleared after the browser tab/window is closed.
