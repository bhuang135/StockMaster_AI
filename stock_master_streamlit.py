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
from translations import (
    LANGUAGE_OPTIONS,
    dataframe_column_label,
    metric_explanation_rows,
    metric_label,
    normalize_language_code,
    t,
)


@st.cache_data(show_spinner=False, ttl=900)
def load_core_data(ticker: str):
    df, fundamentals = get_stock_data(ticker)
    df_pl = get_financial_statements(ticker)
    return df, fundamentals, df_pl


@st.cache_data(show_spinner=False, ttl=900)
def load_fundamentals_with_gemini_fill(ticker: str, fundamentals: dict, api_key: str = ""):
    """
    Fill fields that came back missing / N/A from Yahoo Finance using one
    Gemini + Google Search grounded lookup. This returns the original data
    unchanged when no API key is provided.
    """
    if not api_key:
        return fundamentals
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
    language_code: str = "en",
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
        language_code=language_code,
    )


def build_price_chart(df: pd.DataFrame, ticker: str, language_code: str = "en") -> go.Figure:
    fig = go.Figure(
        data=[
            go.Candlestick(
                x=df.index,
                open=df["Open"],
                high=df["High"],
                low=df["Low"],
                close=df["Close"],
                name=t("price_trace", language_code),
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
        title=t("price_chart_title", language_code, ticker=ticker),
        margin=dict(t=50, b=20, l=20, r=20),
    )
    return fig


def build_pl_chart(df_pl: pd.DataFrame, language_code: str = "en") -> go.Figure:
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=df_pl["Year"],
            y=df_pl["Total Revenue"],
            name=t("total_revenue", language_code),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=df_pl["Year"],
            y=df_pl["Net Income"],
            name=t("net_income", language_code),
            mode="lines+markers",
        )
    )
    fig.update_layout(
        template="plotly_white",
        barmode="group",
        height=400,
        margin=dict(t=20, b=20, l=20, r=20),
    )
    return fig


def render_fundamentals_table(fundamentals: dict, language_code: str = "en") -> pd.DataFrame:
    excluded = {
        "Data Source",
        "Data Period",
        "Symbol",
        "Company Name",
        "Business Summary",
        "Website",
        "_gemini_filled_fields",
    }
    rows = [
        {
            dataframe_column_label("Metric", language_code): metric_label(k, language_code),
            dataframe_column_label("Value", language_code): v,
        }
        for k, v in fundamentals.items()
        if k not in excluded
    ]
    return pd.DataFrame(rows)


def localize_dataframe_columns(df: pd.DataFrame, language_code: str = "en") -> pd.DataFrame:
    if df is None or df.empty:
        return df
    renamed = df.copy()
    renamed.columns = [dataframe_column_label(str(col), language_code) for col in renamed.columns]
    return renamed


def scenario_markdown(
    model_desc: str,
    current_close: float,
    positive_price: float,
    neutral_price: float,
    negative_price: float,
    language_code: str,
) -> str:
    return (
        f"**{t('model_basis', language_code)}:** {model_desc}\n\n"
        f"**{t('current_close', language_code)}:** `${current_close:.2f}`\n\n"
        f"**{t('positive_scenario', language_code)}:** `${positive_price:.2f}`\n\n"
        f"**{t('neutral_scenario', language_code)}:** `${neutral_price:.2f}`\n\n"
        f"**{t('negative_scenario', language_code)}:** `${negative_price:.2f}`"
    )


def main():
    st.set_page_config(
        page_title=t("page_title", "en"),
        page_icon="📈",
        layout="wide",
    )

    if "active_ticker" not in st.session_state:
        st.session_state.active_ticker = "AAPL"
    if "language_code" not in st.session_state:
        st.session_state.language_code = "zh-Hant"

    with st.sidebar:
        language_label = t("language_label", st.session_state.language_code)
        selected_language = st.selectbox(
            language_label,
            options=list(LANGUAGE_OPTIONS.keys()),
            index=list(LANGUAGE_OPTIONS.values()).index(st.session_state.language_code)
            if st.session_state.language_code in LANGUAGE_OPTIONS.values()
            else 0,
            key="language_selector",
        )
        language_code = normalize_language_code(LANGUAGE_OPTIONS[selected_language])
        st.session_state.language_code = language_code

    language_code = st.session_state.language_code

    st.title(t("app_title", language_code))
    st.caption(t("app_caption", language_code))

    with st.sidebar:
        st.header(t("sidebar_header", language_code))

        with st.form(key="ticker_search_form", clear_on_submit=False):
            search_col, button_col = st.columns([3, 1])
            with search_col:
                ticker_input = st.text_input(
                    t("ticker_input", language_code),
                    value=st.session_state.active_ticker,
                    key="ticker_input_field",
                )
            with button_col:
                st.write("")
                st.write("")
                run_analysis = st.form_submit_button(
                    t("search_button", language_code),
                    type="primary",
                    use_container_width=True,
                )
            st.caption(t("ticker_caption", language_code))

        st.markdown("---")
        st.text_input(
            t("gemini_api_key", language_code),
            type="password",
            key="gemini_api_key",
            placeholder=t("gemini_placeholder", language_code),
            help=t("gemini_help", language_code),
        )
        st.caption(t("api_key_caption", language_code))
        st.markdown(t("news_source_caption", language_code))

    ticker = (ticker_input or "").strip().upper()
    gemini_api_key = (st.session_state.get("gemini_api_key") or "").strip()

    if run_analysis and ticker:
        st.session_state.active_ticker = ticker
        st.session_state.pop("chat_answer", None)

    active_ticker = st.session_state.active_ticker

    if not gemini_api_key:
        st.warning(t("missing_api_warning", language_code))

    try:
        with st.spinner(t("loading_data", language_code, ticker=active_ticker)):
            df, fundamentals, df_pl = load_core_data(active_ticker)
            fundamentals = load_fundamentals_with_gemini_fill(
                active_ticker, fundamentals, gemini_api_key
            )

        if df.empty:
            st.error(t("historical_data_error", language_code, ticker=active_ticker))
            return

        (
            current_close,
            positive_price,
            neutral_price,
            negative_price,
            model_desc,
            valuation_debug,
        ) = simulated_valuation(df, fundamentals, api_key=gemini_api_key)

        ai_text = load_ai_plan(
            active_ticker,
            fundamentals,
            current_close,
            model_desc,
            positive_price,
            neutral_price,
            negative_price,
            api_key=gemini_api_key,
            language_code=language_code,
        )

        st.subheader(f"{fundamentals.get('Company Name', active_ticker)} ({active_ticker})")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric(t("current_close", language_code), f"${current_close:.2f}")
        col2.metric(t("positive_scenario", language_code), f"${positive_price:.2f}")
        col3.metric(t("neutral_scenario", language_code), f"${neutral_price:.2f}")
        col4.metric(t("negative_scenario", language_code), f"${negative_price:.2f}")

        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            [
                t("tab_fundamentals", language_code),
                t("tab_price_chart", language_code),
                t("tab_financials_ai", language_code),
                t("tab_chatbot", language_code),
                t("tab_metric_guide", language_code),
            ]
        )

        with tab1:
            st.markdown(t("core_financial_data", language_code))
            st.dataframe(
                render_fundamentals_table(fundamentals, language_code),
                use_container_width=True,
                hide_index=True,
            )
            gemini_filled = fundamentals.get("_gemini_filled_fields") or []
            if gemini_filled:
                localized_fields = [metric_label(field, language_code) for field in gemini_filled]
                st.caption(t("gemini_filled_caption", language_code) + "、".join(localized_fields))
            if fundamentals.get("Business Summary"):
                st.markdown(t("business_summary", language_code))
                st.write(fundamentals.get("Business Summary"))

        with tab2:
            st.markdown(t("technical_analysis", language_code))
            st.plotly_chart(build_price_chart(df, active_ticker, language_code), use_container_width=True)

        with tab3:
            left, right = st.columns([1, 1])
            with left:
                st.markdown(t("five_year_pl", language_code))
                if df_pl is not None and not df_pl.empty:
                    st.dataframe(
                        localize_dataframe_columns(df_pl, language_code),
                        use_container_width=True,
                        hide_index=True,
                    )
                    st.markdown(t("financial_growth_trends", language_code))
                    st.plotly_chart(build_pl_chart(df_pl, language_code), use_container_width=True)
                else:
                    st.info(t("no_financial_data", language_code))

            with right:
                st.markdown(t("simulated_assessment", language_code))
                st.markdown(
                    scenario_markdown(
                        model_desc,
                        current_close,
                        positive_price,
                        neutral_price,
                        negative_price,
                        language_code,
                    )
                )

                with st.expander(t("valuation_debug", language_code)):
                    st.json(valuation_debug)

                st.markdown(t("gemini_plan", language_code))
                st.markdown(ai_text)

                file_stream = generate_docx_report(
                    active_ticker,
                    fundamentals,
                    ai_text,
                    language_code=language_code,
                )
                st.download_button(
                    label=t("download_report", language_code),
                    data=file_stream.getvalue(),
                    file_name=f"StockMaster_{active_ticker}_Report_{language_code}.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    use_container_width=True,
                )

        with tab4:
            st.markdown(t("chatbot_title", language_code))
            question = st.text_area(
                t("question_label", language_code),
                placeholder=t("question_placeholder", language_code),
                key="chat_question",
            )
            ask = st.button(t("ask_ai", language_code), key="ask_ai")

            if ask:
                if not question.strip():
                    st.warning(t("empty_question_warning", language_code))
                elif not gemini_api_key:
                    st.warning(t("api_key_required_warning", language_code))
                else:
                    with st.spinner(t("generating_answer", language_code)):
                        st.session_state.chat_answer = get_ai_chat_response(
                            active_ticker,
                            question,
                            api_key=gemini_api_key,
                            language_code=language_code,
                        )

            if st.session_state.get("chat_answer"):
                st.markdown(st.session_state.chat_answer)

        with tab5:
            st.markdown(t("metric_detail", language_code))
            st.dataframe(
                pd.DataFrame(metric_explanation_rows(language_code)),
                use_container_width=True,
                hide_index=True,
            )

    except Exception as e:
        st.error(f"{t('system_error', language_code)}: {e}")


if __name__ == "__main__":
    main()
