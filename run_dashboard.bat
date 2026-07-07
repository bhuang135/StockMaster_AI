@echo off

:: Activate virtual environment
call .venv\Scripts\activate


:: Run streamlit app
streamlit run stock_master_streamlit.py

pause