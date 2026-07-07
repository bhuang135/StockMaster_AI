# StockMaster AI — GitHub / Streamlit Deployment Guide

這包專案是 **Streamlit Python app**。GitHub 主要用來存放程式碼；如果要讓別人用網址打開 app，建議部署到 **Streamlit Community Cloud**，並連接你的 GitHub repository。

---

## 1. Local test before push

建議先在本機測試：

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

## 2. Push to GitHub

### Option A — Git command line

在 GitHub 建立一個新的空 repo，例如：

```text
StockMaster_AI
```

不要勾選 README、.gitignore、license，因為這包裡面已經有 README 和 .gitignore。

然後在專案資料夾執行：

```bash
cd StockMaster_AI
git init -b main
git add .
git commit -m "Initial commit: StockMaster AI Streamlit app"
git remote add origin https://github.com/YOUR_USERNAME/StockMaster_AI.git
git push -u origin main
```

把 `YOUR_USERNAME` 換成你的 GitHub username。

### Option B — GitHub Desktop

1. Open GitHub Desktop
2. File → Add local repository
3. 選擇 `StockMaster_AI` 資料夾
4. Commit all files
5. Publish repository

---

## 3. Deploy to Streamlit Community Cloud

1. Go to Streamlit Community Cloud
2. Click **Create app**
3. Select your GitHub repo
4. Branch: `main`
5. Main file path:

```text
stock_master_streamlit.py
```

6. In Advanced settings, choose Python 3.12 or newer.
7. Deploy.

---

## 4. API key handling

目前程式沒有把 Gemini API key 寫死在 code 裡。使用者是在 app sidebar 輸入自己的 Gemini API key。

請不要把以下檔案 commit 到 GitHub：

```text
.env
.streamlit/secrets.toml
secrets.toml
```

這些已經被 `.gitignore` 排除。

---

## 5. Important deployment notes

- 這不是靜態網站，所以不能只用 GitHub Pages 直接跑 Streamlit app。
- GitHub 負責存 code；Streamlit Community Cloud / Render / Railway 才是負責跑 app 的地方。
- `requirements.txt` 必須放在 repo root，這包已經處理好。
- 如果 Streamlit Cloud build 失敗，先看 log 裡面是哪個 package 安裝失敗，常見原因是 Python version 或 dependency missing。

