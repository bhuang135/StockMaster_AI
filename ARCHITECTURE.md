# 🧠 StockMaster AI System Architecture

---

# System Overview

User Interface (Streamlit)
        ↓
Application Controller
        ↓
Data Layer
        ↓
Analytics Layer
        ↓
AI Reasoning Layer
        ↓
Visualization Layer

---

# Layer 1 — Frontend (Streamlit)

File:

stock_master_streamlit.py

Responsibilities:

- User input
- Ticker selection
- Dashboard rendering

---

# Layer 2 — Data Retrieval Layer

File:

stock_data_utils_fixed.py

Responsibilities:

- Fetch market data
- Retrieve fundamentals
- Collect news data

Sources:

Yahoo Finance  
Gemini (Google Search grounding)  

### News Aggregation (multi-source)

`get_recent_news()` is a small orchestrator that queries **two
independent sources** in parallel and merges the results, so the
sentiment engine (Layer 3) has broader, more resilient news coverage:

| # | Source | Requires | Behavior if unavailable |
|---|--------|----------|--------------------------|
| 1 | Yahoo Finance (`_get_yahoo_finance_news`, via `yfinance`) | Nothing — always on | Skipped silently on network/schema error |
| 2 | Gemini + Google Search grounding (`_get_gemini_grounded_news`) | The user's own Gemini API key (typed into the search UI) | Skipped silently if no key, if the grounding tool call fails, or if the response isn't actually grounded |

Each source fails independently (try/except per source), so one broken
source never breaks the other. Results are de-duplicated by normalized
title and sorted by recency before being capped at `max_items`.

**Trust boundary for the Gemini source:** the Gemini query uses the
`google_search` grounding tool so its answers are backed by real citation
URLs (`grounding_metadata.grounding_chunks[].web.uri`). If the model
responds without actual grounding metadata (e.g. it just wrote free text
from memory), that response is discarded rather than treated as "news" —
this avoids feeding a possible hallucination into the sentiment/valuation
pipeline.

### Filling missing/"N/A" fundamentals with Gemini

`fill_missing_fundamentals_with_gemini()` runs after `get_stock_data()`.
Any fundamentals field that came back missing from Yahoo Finance (CEO,
sector, P/E ratio, etc.) is collected into a single batched Gemini +
`google_search` grounded lookup (one API call regardless of how many
fields are missing). Same trust boundary as the news sources: the whole
batch is discarded unless the response is actually grounded — a missing
fact stays "N/A" rather than risking a hallucinated CEO name or number.
Fields that *are* filled are recorded in
`fundamentals["_gemini_filled_fields"]` so the UI shows the user which
values came from a live Gemini lookup instead of Yahoo Finance.

---

# Layer 3 — Analytics Layer

Includes:

- Financial metrics calculation
- Sentiment scoring
- Valuation simulation

### Sentiment Scoring Engine (NLP)

File: `stock_data_utils_fixed.py` — `_get_local_sentiment_tag()`

This is a **separate, deterministic NLP component**, distinct from the
LLM/RAG layer below. It does not call Gemini and does not use retrieval —
it is a local lexicon-based classifier that:

1. Takes each news article's headline + description.
2. Matches ~150 curated positive/negative finance phrases against the
   text using phrase-aware regex (a term like `revenue-growth` matches
   both `"revenue-growth"` and `"revenue growth"` in real text).
3. Applies a small negation window (`not`, `no`, `fails`, `unable`, ...)
   so phrases like "not profitable" or "no losses" flip polarity instead
   of being scored blindly.
4. Produces a per-article `raw_score` and a capped `sentiment_weight`
   (±0.03), which `summarize_news_sentiment()` aggregates and clamps to
   `[-0.15, 0.15]`.
5. Feeds into `simulated_valuation()` as `sentiment_total`, which is
   scaled by each valuation model's `sentiment_sensitivity` to bias the
   Positive/Neutral/Negative price scenarios.

**2026-07 fix:** the previous version tokenized text into single words
and checked those against a lexicon made mostly of hyphenated
multi-word phrases (e.g. `record-high`, `earnings-miss`). Since
tokenizing strips hyphens, the tokens could never match the hyphenated
lexicon entries, so most real headlines scored `Neutral` regardless of
content and the sentiment→price-scenario pipeline was effectively
disconnected. This has been fixed with phrase-aware regex matching (see
above) plus the negation window, and scoring now runs on headline +
description instead of headline alone for more signal.

---

# Layer 4 — RAG Chatbot / Report Grounding Layer

File:

rag_chat_pipeline.py (chat) + `_build_rag_corpus()` in
`stock_data_utils_fixed.py` (investment plan report)

Pipeline:

User Question  
→ Query Expansion  
→ Knowledge Retrieval (TF-IDF + cosine similarity)  
→ Ranking  
→ LLM Response (Gemini, grounded with inline citations + optional live
  Google Search)

Note: this layer is intentionally separate from the sentiment scoring
engine in Layer 3. Retrieval decides *which facts* the LLM sees; the
sentiment engine decides *how bullish/bearish* the numeric price
scenarios are. The retrieved news documents do carry the sentiment
engine's `tone_tag` / `raw_score` as metadata so the LLM's narrative
stays consistent with the numeric scenario math, but the two systems
compute independently.

### Live Google Search fallback (chatbot)

The chatbot's retrieval (Layer 4) only searches this app's own local
knowledge base for the current ticker. `generate_chat_answer_with_citations()`
additionally gives the model the `google_search` grounding tool
(`use_search_grounding=True`), so it can fill gaps the local KB doesn't
cover — e.g. a fact that's "N/A" locally, or something more recent than
what was retrieved.

This is deliberately **scoped, not open-ended**: the prompt instructs the
model to only use live search for the current `{ticker}`/`{company_name}`,
never to answer about a different company. Any live-search-derived claim
must be marked `(live search)` in the answer, and real source URLs
extracted from `grounding_metadata` are appended in a separate "Live
Search Sources" section — kept distinct from the numbered `[1] [2]`
citations that point at the local retrieved context, so the two evidence
trails never get confused. If the grounding tool call itself fails
(unsupported SDK/model combo), the chatbot falls back to an ungrounded,
context-only answer rather than failing the whole turn.

---

# Layer 5 — Visualization Layer

Framework:

Streamlit  
Plotly  

Displays:

Tables  
Charts  
AI Reports