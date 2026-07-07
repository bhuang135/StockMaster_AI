# Multilingual Implementation Notes

This version implements built-in language switching instead of relying on browser translation.

## Why built-in translation?

Browser translation is useful as a backup, but it can mistranslate finance terms, tickers, metric labels, or dynamic Streamlit content. Built-in translation gives better control over:

- Financial terminology
- Stock ticker preservation
- Dashboard labels
- AI prompt language
- DOCX report output
- User experience consistency

## Files Added / Updated

```text
translations.py
stock_master_streamlit.py
stock_data_utils_fixed.py
rag_chat_pipeline.py
README.md
SETUP.md
USER_GUIDE.md
```

## Language Codes

```text
zh-Hant = Traditional Chinese
zh-Hans = Simplified Chinese
en      = English
```

## AI Prompt Control

The selected language is passed into:

- `get_ai_investment_plan(..., language_code=...)`
- `get_ai_chat_response(..., language_code=...)`
- `generate_docx_report(..., language_code=...)`

`translations.py` provides the language instruction sent to Gemini.
