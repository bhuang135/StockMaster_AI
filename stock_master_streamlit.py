from __future__ import annotations

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from stock_data_utils_fixed import (
    get_stock_data,
    simulated_valuation,
    get_ai_investment_plan,
    generate_docx_report,
    get_financial_statements,
    get_ai_chat_response,
    fill_missing_fundamentals_with_gemini,
)

METRICS_EXPLANATION = [
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
        "Data Period": "Latest Quarter/Year (Balance Sheet data)",
        "Market Significance": "Risk indicator. Measures the proportion of debt relative to equity in a company's capital structure.",
    },
    {
        "Metric": "Market Cap ($B)",
        "How it's Calculated": "Stock Price * Total Shares Outstanding.",
        "Data Period": "Real-time",
        "Market Significance": "Scale indicator. Measures the total market value of the company.",
    },
    {
        "Metric": "Data Period",
        "How it's Calculated": "Historical stock price data range: Past 5 years (5Y).",
        "Data Period": "Past 5 Years (Used for Candlestick & Technical Analysis)",
        "Market Significance": "Historical analysis timeframe.",
    },
]


@st.cache_data(show_spinner=False, ttl=900)
def load_core_data(ticker: str):
    df, fundamentals = get_stock_data(ticker)
    df_pl = get_financial_statements(ticker)
    return df, fundamentals, df_pl


@st.cache_data(show_spinner=False, ttl=900)
def load_fundamentals_with_gemini_fill(ticker: str, fundamentals: dict, api_key: str = ""):
    """
    Fill any fundamentals field that came back "N/A" / missing from Yahoo
    Finance using a single Gemini + Google Search grounded lookup. No-ops
    (returns fundamentals unchanged) if no API key is provided or nothing
    is missing.
    """
    if not api_key:
        return fundamentals
    # work on a copy so Streamlit's cache never sees the input mutated
    return fill_missing_fundamentals_with_gemini(dict(fundamentals), ticker, api_key=api_key)


@st.cache_data(show_spinner=False, ttl=900)
def load_ai_plan(
    ticker: str,
    fundamentals: dict,
    current_close: float,
    model_desc: str,
    positive_price: float,
    neutral_price: float,
    negative_price: float,
    api_key: str = "",
):
    return get_ai_investment_plan(
        ticker,
        fundamentals,
        current_close,
        model_desc,
        positive_price,
        neutral_price,
        negative_price,
        api_key=api_key,
    )


def build_price_chart(df: pd.DataFrame, ticker: str) -> go.Figure:
    fig = go.Figure(
        data=[
            go.Candlestick(
                x=df.index,
                open=df["Open"],
                high=df["High"],
                low=df["Low"],
                close=df["Close"],
                name="Price",
            )
        ]
    )

    ma_windows = [5, 20, 60, 90, 248]
    for window in ma_windows:
        fig.add_trace(
            go.Scatter(
                x=df.index,
                y=df["Close"].rolling(window=window).mean(),
                mode="lines",
                name=f"MA({window})",
                line={"width": 1},
            )
        )

    fig.update_layout(
        template="plotly_white",
        height=550,
        xaxis_rangeslider_visible=False,
        title=f"{ticker} 5-Year Trend Analysis",
        margin=dict(t=50, b=20, l=20, r=20),
    )
    return fig



def build_pl_chart(df_pl: pd.DataFrame) -> go.Figure:
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df_pl["Year"], y=df_pl["Total Revenue"], name="Total Revenue"))
    fig.add_trace(go.Scatter(x=df_pl["Year"], y=df_pl["Net Income"], name="Net Income", mode="lines+markers"))
    fig.update_layout(
        template="plotly_white",
        barmode="group",
        height=400,
        margin=dict(t=20, b=20, l=20, r=20),
    )
    return fig



def render_fundamentals_table(fundamentals: dict) -> pd.DataFrame:
    excluded = {
        "Data Source", "Data Period", "Symbol", "Company Name",
        "Business Summary", "Website", "_gemini_filled_fields",
    }
    rows = [{"Metric": k, "Value": v} for k, v in fundamentals.items() if k not in excluded]
    return pd.DataFrame(rows)



def main():
    st.set_page_config(
        page_title="StockMaster Streamlit Demo",
        page_icon="????",
        layout="wide",
    )

    st.title("StockMaster Integrated Analysis Dashboard")
    st.caption("Streamlit demo version converted from your Dash architecture.")

    if "active_ticker" not in st.session_state:
        st.session_state.active_ticker = "AAPL"

    with st.sidebar:
        st.header("標的查詢 / Demo Controls")

        # --- Ticker search: input + Search button, Enter key also submits ---
        with st.form(key="ticker_search_form", clear_on_submit=False):
            search_col, button_col = st.columns([3, 1])
            with search_col:
                ticker_input = st.text_input(
                    "Enter Stock Ticker",
                    value=st.session_state.active_ticker,
                    key="ticker_input_field",
                )
            with button_col:
                st.write("")  # vertical spacer to align button with input
                st.write("")
                run_analysis = st.form_submit_button(
                    "Search", type="primary", use_container_width=True
                )
            st.caption("輸入股票代碼後按 Enter 或點擊 Search 按鈕即可開始查詢。")

        # --- Gemini API Key: user-supplied, cached only for this browser session ---
        st.markdown("---")
        st.text_input(
            "Gemini API Key",
            type="password",
            key="gemini_api_key",
            placeholder="請輸入您自己的 Gemini API Key",
            help=(
                "此金鑰僅暫存於您目前的瀏覽器工作階段（session），"
                "不會寫入程式碼、不會存到伺服器端檔案；"
                "關閉瀏覽器分頁/視窗後即自動清除，下次需重新輸入。"
            ),
        )
        st.caption(
            "🔒 API Key 僅保存在本次瀏覽器 Session，不會寫死在程式中。"
            "請至 Google AI Studio 取得您自己的 Gemini API Key。"
        )
        st.markdown(
            "新聞來源：Yahoo Finance（自動）＋ Gemini Google Search grounding（需上方 API Key）。"
        )

    ticker = (ticker_input or "").strip().upper()
    gemini_api_key = (st.session_state.get("gemini_api_key") or "").strip()

    if run_analysis and ticker:
        st.session_state.active_ticker = ticker
        st.session_state.pop("chat_answer", None)

    active_ticker = st.session_state.active_ticker

    if not gemini_api_key:
        st.warning(
            "尚未輸入 Gemini API Key，AI 投資建議與 Chatbot 功能將無法使用。"
            "請於左側欄位輸入您自己的 Gemini API Key（僅暫存於本次瀏覽器 Session）。"
        )

    try:
        with st.spinner(f"Loading data for {active_ticker}..."):
            df, fundamentals, df_pl = load_core_data(active_ticker)
            fundamentals = load_fundamentals_with_gemini_fill(
                active_ticker, fundamentals, gemini_api_key
            )

        if df.empty:
            st.error(f"Unable to fetch historical data for {active_ticker}.")
            return

        current_close, positive_price, neutral_price, negative_price, model_desc, valuation_debug = simulated_valuation(
            df, fundamentals, api_key=gemini_api_key
        )
        ai_text = load_ai_plan(
            active_ticker,
            fundamentals,
            current_close,
            model_desc,
            positive_price,
            neutral_price,
            negative_price,
            api_key=gemini_api_key,
        )

        st.subheader(f"{fundamentals.get('Company Name', active_ticker)} ({active_ticker})")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Current Close", f"${current_close:.2f}")
        col2.metric("Positive Scenario", f"${positive_price:.2f}")
        col3.metric("Neutral Scenario", f"${neutral_price:.2f}")
        col4.metric("Negative Scenario", f"${negative_price:.2f}")

        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            [
                "Fundamentals",
                "Price Chart",
                "Financials & AI Plan",
                "Chatbot",
                "Metric Guide",
            ]
        )

        with tab1:
            st.markdown("### Core Financial Data (TTM)")
            st.dataframe(render_fundamentals_table(fundamentals), use_container_width=True, hide_index=True)
            gemini_filled = fundamentals.get("_gemini_filled_fields") or []
            if gemini_filled:
                st.caption(
                    "🔎 以下欄位原本為 N/A，已透過 Gemini + Google Search 即時搜尋補全："
                    + "、".join(gemini_filled)
                )
            if fundamentals.get("Business Summary"):
                st.markdown("### Business Summary")
                st.write(fundamentals.get("Business Summary"))

        with tab2:
            st.markdown("### Technical Analysis (MA Multi-Moving Average System)")
            st.plotly_chart(build_price_chart(df, active_ticker), use_container_width=True)

        with tab3:
            left, right = st.columns([1, 1])
            with left:
                st.markdown("### 5-Year Summary P&L (Unit: $M)")
                if df_pl is not None and not df_pl.empty:
                    st.dataframe(df_pl, use_container_width=True, hide_index=True)
                    st.markdown("### Financial Growth Trends")
                    st.plotly_chart(build_pl_chart(df_pl), use_container_width=True)
                else:
                    st.info("No financial statement data available.")

            with right:
                st.markdown("### Simulated Price Forward Assessment")
                st.markdown(
                    f"**Model Basis:** {model_desc}\n\n"
                    f"**Current Close:** `${current_close:.2f}`\n\n"
                    f"**Positive Scenario:** `${positive_price:.2f}`\n\n"
                    f"**Neutral Scenario:** `${neutral_price:.2f}`\n\n"
                    f"**Negative Scenario:** `${negative_price:.2f}`"
                )

                with st.expander("Valuation debug details"):
                    st.json(valuation_debug)

                st.markdown("### Gemini AI Institutional Investment Plan")
                st.markdown(ai_text)

                file_stream = generate_docx_report(active_ticker, fundamentals, ai_text)
                st.download_button(
                    label="Download Professional Investment Report (.docx)",
                    data=file_stream.getvalue(),
                    file_name=f"StockMaster_{active_ticker}_Report.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    use_container_width=True,
                )

        with tab4:
            st.markdown("### AI Investment Chatbot")
            question = st.text_area("Ask anything about this stock", placeholder="e.g. Who is the CEO of AAPL?", key="chat_question")
            ask = st.button("Ask AI", key="ask_ai")

            if ask:
                if not question.strip():
                    st.warning("Please enter a question.")
                elif not gemini_api_key:
                    st.warning("請先於左側欄位輸入您的 Gemini API Key。")
                else:
                    with st.spinner("Generating grounded answer..."):
                        st.session_state.chat_answer = get_ai_chat_response(
                            active_ticker, question, api_key=gemini_api_key
                        )

            if st.session_state.get("chat_answer"):
                st.markdown(st.session_state.chat_answer)

        with tab5:
            st.markdown("### Core Financial Metrics Detail")
            st.dataframe(pd.DataFrame(METRICS_EXPLANATION), use_container_width=True, hide_index=True)

    except Exception as e:
        st.error(f"System Error: {e}")


if __name__ == "__main__":
    main()
