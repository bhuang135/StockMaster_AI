# ⚙️ StockMaster AI Setup Guide

---

# Step 1 — Install Python

Recommended:

Python 3.12+ recommended for cloud deployment

Check:

python --version

---

# Step 2 — Create Virtual Environment

python -m venv venv

Activate:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

---

# Step 3 — Install Dependencies

pip install -r requirements.txt

---

# Step 4 — API Keys

Gemini API Key is NOT set as an environment variable or hardcoded
anywhere in the code. Instead, each user enters their own Gemini API Key
directly in the app's sidebar (標的查詢介面) when it's running. The key is
only cached in the browser session (cleared when the browser is closed) and
is never written to disk or committed to the repo.

No other API keys are required. News is gathered automatically from
Yahoo Finance (no key needed) and, if you provide a Gemini API Key, also
from a Google Search-grounded Gemini query.

---

# Step 5 — Run Application

streamlit run stock_master_streamlit.py

Or:

run_dashboard.bat

---

# Step 6 — Open Browser

http://localhost:8501

---

# GitHub / Cloud Deployment

See `GITHUB_DEPLOY.md` for the recommended GitHub and Streamlit Community Cloud deployment workflow.
