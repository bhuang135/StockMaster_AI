"""Translation helpers for StockMaster AI.

The app intentionally uses a small built-in dictionary instead of browser
translation so financial labels, risk wording, and AI prompts stay consistent.
Supported languages:
- zh-Hant: Traditional Chinese
- zh-Hans: Simplified Chinese
- en: English
"""

from __future__ import annotations

from typing import Dict

LANGUAGE_OPTIONS: Dict[str, str] = {
    "繁體中文": "zh-Hant",
    "简体中文": "zh-Hans",
    "English": "en",
}

LANGUAGE_DISPLAY: Dict[str, str] = {
    "zh-Hant": "繁體中文",
    "zh-Hans": "简体中文",
    "en": "English",
}

TEXT: Dict[str, Dict[str, str]] = {
    "page_title": {
        "zh-Hant": "StockMaster AI 股票分析助手",
        "zh-Hans": "StockMaster AI 股票分析助手",
        "en": "StockMaster AI Stock Analysis Assistant",
    },
    "app_title": {
        "zh-Hant": "StockMaster AI 整合式股票分析儀表板",
        "zh-Hans": "StockMaster AI 整合式股票分析仪表板",
        "en": "StockMaster AI Integrated Stock Analysis Dashboard",
    },
    "app_caption": {
        "zh-Hant": "結合 Yahoo Finance、技術指標、財務資料、新聞情緒、Gemini AI 與 RAG Chatbot 的投資研究工具。",
        "zh-Hans": "结合 Yahoo Finance、技术指标、财务数据、新闻情绪、Gemini AI 与 RAG Chatbot 的投资研究工具。",
        "en": "Investment research tool combining Yahoo Finance, technical indicators, financials, news sentiment, Gemini AI, and a RAG chatbot.",
    },
    "language_label": {
        "zh-Hant": "介面語言 / Language",
        "zh-Hans": "界面语言 / Language",
        "en": "Language / 語言",
    },
    "sidebar_header": {
        "zh-Hant": "標的查詢與控制台",
        "zh-Hans": "标的查询与控制台",
        "en": "Ticker Search & Controls",
    },
    "ticker_input": {
        "zh-Hant": "請輸入股票代號",
        "zh-Hans": "请输入股票代码",
        "en": "Enter Stock Ticker",
    },
    "search_button": {
        "zh-Hant": "查詢",
        "zh-Hans": "查询",
        "en": "Search",
    },
    "ticker_caption": {
        "zh-Hant": "輸入股票代碼後按 Enter 或點擊查詢按鈕即可開始分析。",
        "zh-Hans": "输入股票代码后按 Enter 或点击查询按钮即可开始分析。",
        "en": "Enter a ticker, then press Enter or click Search to start analysis.",
    },
    "gemini_api_key": {
        "zh-Hant": "Gemini API Key",
        "zh-Hans": "Gemini API Key",
        "en": "Gemini API Key",
    },
    "gemini_placeholder": {
        "zh-Hant": "請輸入您自己的 Gemini API Key",
        "zh-Hans": "请输入您自己的 Gemini API Key",
        "en": "Enter your own Gemini API Key",
    },
    "gemini_help": {
        "zh-Hant": "此金鑰僅暫存於目前瀏覽器工作階段，不會寫入程式碼或伺服器檔案；關閉分頁或視窗後即清除。",
        "zh-Hans": "此密钥仅暂存在当前浏览器会话中，不会写入代码或服务器文件；关闭标签页或窗口后即清除。",
        "en": "This key is kept only in your current browser session. It is not written to code or server files and is cleared when the tab/window closes.",
    },
    "api_key_caption": {
        "zh-Hant": "🔒 API Key 僅保存在本次瀏覽器 Session，不會寫死在程式中。請至 Google AI Studio 取得您自己的 Gemini API Key。",
        "zh-Hans": "🔒 API Key 仅保存在本次浏览器 Session，不会写死在代码中。请至 Google AI Studio 获取您自己的 Gemini API Key。",
        "en": "🔒 The API Key is only stored in this browser session and is not hardcoded. Get your own Gemini API Key from Google AI Studio.",
    },
    "news_source_caption": {
        "zh-Hant": "新聞來源：Yahoo Finance（自動）＋ Gemini Google Search grounding（需上方 API Key）。",
        "zh-Hans": "新闻来源：Yahoo Finance（自动）＋ Gemini Google Search grounding（需要上方 API Key）。",
        "en": "News sources: Yahoo Finance automatically + Gemini Google Search grounding when an API key is provided.",
    },
    "missing_api_warning": {
        "zh-Hant": "尚未輸入 Gemini API Key，AI 投資建議與 Chatbot 功能將無法使用。請於左側欄位輸入您自己的 Gemini API Key（僅暫存於本次瀏覽器 Session）。",
        "zh-Hans": "尚未输入 Gemini API Key，AI 投资建议与 Chatbot 功能将无法使用。请于左侧栏位输入您自己的 Gemini API Key（仅暂存在本次浏览器 Session）。",
        "en": "Gemini API Key is missing. AI investment plan and chatbot features will be unavailable until you enter your own key in the sidebar.",
    },
    "loading_data": {
        "zh-Hant": "正在載入 {ticker} 的資料...",
        "zh-Hans": "正在加载 {ticker} 的数据...",
        "en": "Loading data for {ticker}...",
    },
    "historical_data_error": {
        "zh-Hant": "無法取得 {ticker} 的歷史資料。",
        "zh-Hans": "无法取得 {ticker} 的历史数据。",
        "en": "Unable to fetch historical data for {ticker}.",
    },
    "current_close": {
        "zh-Hant": "目前收盤價",
        "zh-Hans": "当前收盘价",
        "en": "Current Close",
    },
    "positive_scenario": {
        "zh-Hant": "正向情境",
        "zh-Hans": "正向情景",
        "en": "Positive Scenario",
    },
    "neutral_scenario": {
        "zh-Hant": "中性情境",
        "zh-Hans": "中性情景",
        "en": "Neutral Scenario",
    },
    "negative_scenario": {
        "zh-Hant": "負向情境",
        "zh-Hans": "负向情景",
        "en": "Negative Scenario",
    },
    "tab_fundamentals": {
        "zh-Hant": "基本面",
        "zh-Hans": "基本面",
        "en": "Fundamentals",
    },
    "tab_price_chart": {
        "zh-Hant": "價格圖表",
        "zh-Hans": "价格图表",
        "en": "Price Chart",
    },
    "tab_financials_ai": {
        "zh-Hant": "財報與 AI 計畫",
        "zh-Hans": "财报与 AI 计划",
        "en": "Financials & AI Plan",
    },
    "tab_chatbot": {
        "zh-Hant": "AI 聊天機器人",
        "zh-Hans": "AI 聊天机器人",
        "en": "Chatbot",
    },
    "tab_metric_guide": {
        "zh-Hant": "指標說明",
        "zh-Hans": "指标说明",
        "en": "Metric Guide",
    },
    "core_financial_data": {
        "zh-Hant": "### 核心財務資料（TTM）",
        "zh-Hans": "### 核心财务数据（TTM）",
        "en": "### Core Financial Data (TTM)",
    },
    "gemini_filled_caption": {
        "zh-Hant": "🔎 以下欄位原本為 N/A，已透過 Gemini + Google Search 即時搜尋補全：",
        "zh-Hans": "🔎 以下字段原本为 N/A，已通过 Gemini + Google Search 实时搜索补全：",
        "en": "🔎 These fields were originally N/A and were filled by Gemini + Google Search: ",
    },
    "business_summary": {
        "zh-Hant": "### 業務摘要",
        "zh-Hans": "### 业务摘要",
        "en": "### Business Summary",
    },
    "technical_analysis": {
        "zh-Hant": "### 技術分析（多均線系統）",
        "zh-Hans": "### 技术分析（多均线系统）",
        "en": "### Technical Analysis (MA Multi-Moving Average System)",
    },
    "five_year_pl": {
        "zh-Hant": "### 五年損益摘要（單位：百萬美元）",
        "zh-Hans": "### 五年损益摘要（单位：百万美元）",
        "en": "### 5-Year Summary P&L (Unit: $M)",
    },
    "financial_growth_trends": {
        "zh-Hant": "### 財務成長趨勢",
        "zh-Hans": "### 财务成长趋势",
        "en": "### Financial Growth Trends",
    },
    "no_financial_data": {
        "zh-Hant": "目前沒有可用的財務報表資料。",
        "zh-Hans": "目前没有可用的财务报表数据。",
        "en": "No financial statement data available.",
    },
    "simulated_assessment": {
        "zh-Hant": "### 模擬股價前瞻評估",
        "zh-Hans": "### 模拟股价前瞻评估",
        "en": "### Simulated Price Forward Assessment",
    },
    "model_basis": {
        "zh-Hant": "模型基礎",
        "zh-Hans": "模型基础",
        "en": "Model Basis",
    },
    "valuation_debug": {
        "zh-Hant": "估值模型 debug 細節",
        "zh-Hans": "估值模型 debug 细节",
        "en": "Valuation debug details",
    },
    "gemini_plan": {
        "zh-Hant": "### Gemini AI 機構級投資分析計畫",
        "zh-Hans": "### Gemini AI 机构级投资分析计划",
        "en": "### Gemini AI Institutional Investment Plan",
    },
    "download_report": {
        "zh-Hant": "下載專業投資報告（.docx）",
        "zh-Hans": "下载专业投资报告（.docx）",
        "en": "Download Professional Investment Report (.docx)",
    },
    "chatbot_title": {
        "zh-Hant": "### AI 投資聊天機器人",
        "zh-Hans": "### AI 投资聊天机器人",
        "en": "### AI Investment Chatbot",
    },
    "question_label": {
        "zh-Hant": "輸入你想問這檔股票的問題",
        "zh-Hans": "输入你想问这只股票的问题",
        "en": "Ask anything about this stock",
    },
    "question_placeholder": {
        "zh-Hant": "例如：AAPL 的 CEO 是誰？近期股價下跌原因是什麼？",
        "zh-Hans": "例如：AAPL 的 CEO 是谁？近期股价下跌原因是什么？",
        "en": "e.g. Who is the CEO of AAPL? What caused the recent price movement?",
    },
    "ask_ai": {
        "zh-Hant": "詢問 AI",
        "zh-Hans": "询问 AI",
        "en": "Ask AI",
    },
    "empty_question_warning": {
        "zh-Hant": "請先輸入問題。",
        "zh-Hans": "请先输入问题。",
        "en": "Please enter a question.",
    },
    "api_key_required_warning": {
        "zh-Hant": "請先於左側欄位輸入您的 Gemini API Key。",
        "zh-Hans": "请先于左侧栏位输入您的 Gemini API Key。",
        "en": "Please enter your Gemini API Key in the sidebar first.",
    },
    "generating_answer": {
        "zh-Hant": "正在產生有依據的回答...",
        "zh-Hans": "正在生成有依据的回答...",
        "en": "Generating grounded answer...",
    },
    "metric_detail": {
        "zh-Hant": "### 核心財務指標說明",
        "zh-Hans": "### 核心财务指标说明",
        "en": "### Core Financial Metrics Detail",
    },
    "system_error": {
        "zh-Hant": "系統錯誤",
        "zh-Hans": "系统错误",
        "en": "System Error",
    },
    "price_chart_title": {
        "zh-Hant": "{ticker} 五年趨勢分析",
        "zh-Hans": "{ticker} 五年趋势分析",
        "en": "{ticker} 5-Year Trend Analysis",
    },
    "price_trace": {
        "zh-Hant": "價格",
        "zh-Hans": "价格",
        "en": "Price",
    },
    "total_revenue": {
        "zh-Hant": "總營收",
        "zh-Hans": "总营收",
        "en": "Total Revenue",
    },
    "net_income": {
        "zh-Hant": "淨利",
        "zh-Hans": "净利润",
        "en": "Net Income",
    },
    "metric_col": {
        "zh-Hant": "指標",
        "zh-Hans": "指标",
        "en": "Metric",
    },
    "value_col": {
        "zh-Hant": "數值",
        "zh-Hans": "数值",
        "en": "Value",
    },
    "year_col": {
        "zh-Hant": "年度",
        "zh-Hans": "年度",
        "en": "Year",
    },
    "how_calculated_col": {
        "zh-Hant": "計算方式",
        "zh-Hans": "计算方式",
        "en": "How it's Calculated",
    },
    "data_period_col": {
        "zh-Hant": "資料期間",
        "zh-Hans": "数据期间",
        "en": "Data Period",
    },
    "market_significance_col": {
        "zh-Hant": "市場意義",
        "zh-Hans": "市场意义",
        "en": "Market Significance",
    },
}

METRIC_LABELS: Dict[str, Dict[str, str]] = {
    "Symbol": {"zh-Hant": "股票代號", "zh-Hans": "股票代码", "en": "Symbol"},
    "Company Name": {"zh-Hant": "公司名稱", "zh-Hans": "公司名称", "en": "Company Name"},
    "CEO": {"zh-Hant": "執行長", "zh-Hans": "首席执行官", "en": "CEO"},
    "CFO": {"zh-Hant": "財務長", "zh-Hans": "首席财务官", "en": "CFO"},
    "Founder": {"zh-Hant": "創辦人", "zh-Hans": "创始人", "en": "Founder"},
    "P/E Ratio (TTM)": {"zh-Hant": "本益比（TTM）", "zh-Hans": "市盈率（TTM）", "en": "P/E Ratio (TTM)"},
    "Forward P/E": {"zh-Hant": "預估本益比", "zh-Hans": "预估市盈率", "en": "Forward P/E"},
    "Revenue Growth (YoY)": {"zh-Hant": "營收年增率", "zh-Hans": "营收同比增长率", "en": "Revenue Growth (YoY)"},
    "Profit Margin": {"zh-Hant": "淨利率", "zh-Hans": "净利润率", "en": "Profit Margin"},
    "ROE (Return on Equity)": {"zh-Hant": "股東權益報酬率（ROE）", "zh-Hans": "净资产收益率（ROE）", "en": "ROE (Return on Equity)"},
    "Debt/Equity": {"zh-Hant": "負債權益比", "zh-Hans": "负债权益比", "en": "Debt/Equity"},
    "Market Cap": {"zh-Hant": "市值", "zh-Hans": "市值", "en": "Market Cap"},
    "Market Cap ($B)": {"zh-Hant": "市值（十億美元）", "zh-Hans": "市值（十亿美元）", "en": "Market Cap ($B)"},
    "Sector": {"zh-Hant": "產業板塊", "zh-Hans": "行业板块", "en": "Sector"},
    "Industry": {"zh-Hant": "細分產業", "zh-Hans": "细分行业", "en": "Industry"},
    "Business Summary": {"zh-Hant": "業務摘要", "zh-Hans": "业务摘要", "en": "Business Summary"},
    "Website": {"zh-Hant": "官方網站", "zh-Hans": "官方网站", "en": "Website"},
    "Headquarters": {"zh-Hant": "總部", "zh-Hans": "总部", "en": "Headquarters"},
    "Country": {"zh-Hant": "國家", "zh-Hans": "国家", "en": "Country"},
    "Full Time Employees": {"zh-Hant": "全職員工數", "zh-Hans": "全职员工数", "en": "Full Time Employees"},
    "Exchange": {"zh-Hant": "交易所", "zh-Hans": "交易所", "en": "Exchange"},
    "Currency": {"zh-Hant": "幣別", "zh-Hans": "币种", "en": "Currency"},
    "Data Period": {"zh-Hant": "資料期間", "zh-Hans": "数据期间", "en": "Data Period"},
}

DATAFRAME_COLUMNS: Dict[str, Dict[str, str]] = {
    "Year": {"zh-Hant": "年度", "zh-Hans": "年度", "en": "Year"},
    "Total Revenue": {"zh-Hant": "總營收", "zh-Hans": "总营收", "en": "Total Revenue"},
    "Net Income": {"zh-Hant": "淨利", "zh-Hans": "净利润", "en": "Net Income"},
    "Gross Profit": {"zh-Hant": "毛利", "zh-Hans": "毛利", "en": "Gross Profit"},
    "Operating Income": {"zh-Hant": "營業利益", "zh-Hans": "营业利润", "en": "Operating Income"},
    "Metric": {"zh-Hant": "指標", "zh-Hans": "指标", "en": "Metric"},
    "Value": {"zh-Hant": "數值", "zh-Hans": "数值", "en": "Value"},
    "How it's Calculated": {"zh-Hant": "計算方式", "zh-Hans": "计算方式", "en": "How it's Calculated"},
    "Data Period": {"zh-Hant": "資料期間", "zh-Hans": "数据期间", "en": "Data Period"},
    "Market Significance": {"zh-Hant": "市場意義", "zh-Hans": "市场意义", "en": "Market Significance"},
}

LANGUAGE_INSTRUCTIONS: Dict[str, str] = {
    "zh-Hant": "請使用繁體中文回答，並使用台灣常用金融與投資研究用語。保留股票代號、公司英文名稱、財務比率縮寫與引用連結原文，不要改寫 ticker。",
    "zh-Hans": "请使用简体中文回答，并使用中国大陆常用金融与投资研究术语。保留股票代码、公司英文名称、财务比率缩写与引用链接原文，不要改写 ticker。",
    "en": "Please answer in professional English. Keep tickers, company names, financial ratio abbreviations, and source links unchanged.",
}

DOCX_TEXT: Dict[str, Dict[str, str]] = {
    "title": {
        "zh-Hant": "StockMaster 研究報告：{ticker}",
        "zh-Hans": "StockMaster 研究报告：{ticker}",
        "en": "StockMaster Research: {ticker}",
    },
    "fundamental_summary": {
        "zh-Hant": "I. 基本面摘要",
        "zh-Hans": "I. 基本面摘要",
        "en": "I. Fundamental Summary",
    },
    "integrated_analysis": {
        "zh-Hant": "II. 整合分析與新聞摘要",
        "zh-Hans": "II. 整合分析与新闻摘要",
        "en": "II. Integrated Analysis & News Feed",
    },
    "disclaimer_title": {
        "zh-Hant": "免責聲明",
        "zh-Hans": "免责声明",
        "en": "Disclaimer",
    },
    "disclaimer": {
        "zh-Hant": "本 AI 產生報告僅供研究與學習用途，不構成投資、法律、稅務或財務建議。",
        "zh-Hans": "本 AI 生成报告仅供研究与学习用途，不构成投资、法律、税务或财务建议。",
        "en": "This AI-generated report is for research only and does not constitute financial advice.",
    },
}

METRICS_EXPLANATION_BY_LANG = {
    "en": [
        {
            "Metric": "P/E Ratio (TTM)",
            "How it's Calculated": "Stock Price / Earnings Per Share (EPS) over the past twelve months (TTM).",
            "Data Period": "Past 12 Months",
            "Market Significance": "Value indicator. Measures valuation levels.",
        },
        {
            "Metric": "Forward P/E",
            "How it's Calculated": "Stock Price / Projected Earnings Per Share (EPS) for the next twelve months.",
            "Data Period": "Next 12 Months (Earnings Forecast)",
            "Market Significance": "Expectation indicator. Based on analyst consensus forecasts for future earnings.",
        },
        {
            "Metric": "Revenue Growth (YoY)",
            "How it's Calculated": "Percentage change between total revenue of the latest reporting period and the same period last year.",
            "Data Period": "Latest Quarter/Year (YoY Comparison)",
            "Market Significance": "Growth indicator. Measures the speed of the company's revenue growth.",
        },
        {
            "Metric": "Profit Margin",
            "How it's Calculated": "Net Income / Total Revenue.",
            "Data Period": "Past 12 Months (TTM)",
            "Market Significance": "Efficiency indicator. Measures how much net profit a company generates per $1 of revenue.",
        },
        {
            "Metric": "ROE (Return on Equity)",
            "How it's Calculated": "Net Income / Shareholder's Equity.",
            "Data Period": "Past 12 Months (TTM)",
            "Market Significance": "Efficiency indicator. Measures a company's ability to generate profit using shareholders' capital.",
        },
        {
            "Metric": "Debt/Equity",
            "How it's Calculated": "Total Debt / Shareholder's Equity.",
            "Data Period": "Latest Quarter/Year Balance Sheet data",
            "Market Significance": "Risk indicator. Measures the proportion of debt relative to equity in a company's capital structure.",
        },
        {
            "Metric": "Market Cap ($B)",
            "How it's Calculated": "Stock Price * Total Shares Outstanding.",
            "Data Period": "Real-time / latest available market data",
            "Market Significance": "Scale indicator. Measures the total market value of the company.",
        },
        {
            "Metric": "Data Period",
            "How it's Calculated": "Historical stock price data range: past 5 years.",
            "Data Period": "Past 5 Years",
            "Market Significance": "Historical analysis timeframe used for candlestick and technical analysis.",
        },
    ],
    "zh-Hant": [
        {
            "Metric": "本益比（TTM）",
            "How it's Calculated": "股價 / 過去十二個月每股盈餘（EPS）。",
            "Data Period": "過去十二個月",
            "Market Significance": "估值指標，用來衡量股價相對獲利是否偏高或偏低。",
        },
        {
            "Metric": "預估本益比",
            "How it's Calculated": "股價 / 未來十二個月預估每股盈餘。",
            "Data Period": "未來十二個月盈餘預估",
            "Market Significance": "市場預期指標，反映分析師對未來獲利的共識。",
        },
        {
            "Metric": "營收年增率",
            "How it's Calculated": "最近一期營收相較去年同期的百分比變化。",
            "Data Period": "最近一季或最近一年，與去年同期比較",
            "Market Significance": "成長指標，用來觀察公司營收擴張速度。",
        },
        {
            "Metric": "淨利率",
            "How it's Calculated": "淨利 / 總營收。",
            "Data Period": "過去十二個月",
            "Market Significance": "經營效率指標，衡量每 1 美元營收可轉化為多少淨利。",
        },
        {
            "Metric": "股東權益報酬率（ROE）",
            "How it's Calculated": "淨利 / 股東權益。",
            "Data Period": "過去十二個月",
            "Market Significance": "資本效率指標，衡量公司運用股東資本創造獲利的能力。",
        },
        {
            "Metric": "負債權益比",
            "How it's Calculated": "總負債 / 股東權益。",
            "Data Period": "最近一季或最近一年資產負債表資料",
            "Market Significance": "風險指標，衡量公司資本結構中負債相對於權益的比重。",
        },
        {
            "Metric": "市值（十億美元）",
            "How it's Calculated": "股價 × 流通在外股數。",
            "Data Period": "即時或最近可得市場資料",
            "Market Significance": "公司規模指標，衡量市場給予公司的總價值。",
        },
        {
            "Metric": "資料期間",
            "How it's Calculated": "歷史股價資料區間：過去五年。",
            "Data Period": "過去五年",
            "Market Significance": "用於 K 線圖與技術分析的歷史分析期間。",
        },
    ],
    "zh-Hans": [
        {
            "Metric": "市盈率（TTM）",
            "How it's Calculated": "股价 / 过去十二个月每股收益（EPS）。",
            "Data Period": "过去十二个月",
            "Market Significance": "估值指标，用来衡量股价相对盈利是否偏高或偏低。",
        },
        {
            "Metric": "预估市盈率",
            "How it's Calculated": "股价 / 未来十二个月预估每股收益。",
            "Data Period": "未来十二个月盈利预测",
            "Market Significance": "市场预期指标，反映分析师对未来盈利的共识。",
        },
        {
            "Metric": "营收同比增长率",
            "How it's Calculated": "最近一期营收相较去年同期的百分比变化。",
            "Data Period": "最近一季或最近一年，与去年同期比较",
            "Market Significance": "成长指标，用来观察公司营收扩张速度。",
        },
        {
            "Metric": "净利润率",
            "How it's Calculated": "净利润 / 总营收。",
            "Data Period": "过去十二个月",
            "Market Significance": "经营效率指标，衡量每 1 美元营收可转化为多少净利润。",
        },
        {
            "Metric": "净资产收益率（ROE）",
            "How it's Calculated": "净利润 / 股东权益。",
            "Data Period": "过去十二个月",
            "Market Significance": "资本效率指标，衡量公司运用股东资本创造盈利的能力。",
        },
        {
            "Metric": "负债权益比",
            "How it's Calculated": "总负债 / 股东权益。",
            "Data Period": "最近一季或最近一年资产负债表数据",
            "Market Significance": "风险指标，衡量公司资本结构中负债相对于权益的比重。",
        },
        {
            "Metric": "市值（十亿美元）",
            "How it's Calculated": "股价 × 流通在外股数。",
            "Data Period": "实时或最近可得市场数据",
            "Market Significance": "公司规模指标，衡量市场给予公司的总价值。",
        },
        {
            "Metric": "数据期间",
            "How it's Calculated": "历史股价数据区间：过去五年。",
            "Data Period": "过去五年",
            "Market Significance": "用于 K 线图与技术分析的历史分析期间。",
        },
    ],
}


def normalize_language_code(language_code: str | None) -> str:
    """Normalize supported language aliases to the internal language code."""
    if not language_code:
        return "en"
    code = str(language_code).strip()
    alias_map = {
        "zh-TW": "zh-Hant",
        "zh_Hant": "zh-Hant",
        "traditional": "zh-Hant",
        "繁體中文": "zh-Hant",
        "zh-CN": "zh-Hans",
        "zh_Hans": "zh-Hans",
        "simplified": "zh-Hans",
        "简体中文": "zh-Hans",
        "english": "en",
        "English": "en",
    }
    code = alias_map.get(code, code)
    return code if code in {"zh-Hant", "zh-Hans", "en"} else "en"


def t(key: str, language_code: str = "en", **kwargs) -> str:
    """Translate a UI text key and apply optional .format(**kwargs)."""
    lang = normalize_language_code(language_code)
    value = TEXT.get(key, {}).get(lang) or TEXT.get(key, {}).get("en") or key
    if kwargs:
        try:
            return value.format(**kwargs)
        except Exception:
            return value
    return value


def metric_label(label: str, language_code: str = "en") -> str:
    lang = normalize_language_code(language_code)
    return METRIC_LABELS.get(label, {}).get(lang) or METRIC_LABELS.get(label, {}).get("en") or label


def dataframe_column_label(label: str, language_code: str = "en") -> str:
    lang = normalize_language_code(language_code)
    return DATAFRAME_COLUMNS.get(label, {}).get(lang) or DATAFRAME_COLUMNS.get(label, {}).get("en") or label


def language_instruction(language_code: str = "en") -> str:
    lang = normalize_language_code(language_code)
    return LANGUAGE_INSTRUCTIONS.get(lang, LANGUAGE_INSTRUCTIONS["en"])


def docx_text(key: str, language_code: str = "en", **kwargs) -> str:
    lang = normalize_language_code(language_code)
    value = DOCX_TEXT.get(key, {}).get(lang) or DOCX_TEXT.get(key, {}).get("en") or key
    if kwargs:
        try:
            return value.format(**kwargs)
        except Exception:
            return value
    return value


def metric_explanation_rows(language_code: str = "en") -> list[dict[str, str]]:
    lang = normalize_language_code(language_code)
    rows = METRICS_EXPLANATION_BY_LANG.get(lang, METRICS_EXPLANATION_BY_LANG["en"])
    translated_rows = []
    for row in rows:
        translated_rows.append({
            dataframe_column_label(k, lang): v for k, v in row.items()
        })
    return translated_rows
