import os
import streamlit as st
from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI

from src.fetch_Data import fetch_stock_data
from src.create_index import create_index_from_stock_data
from src.query_engine import query_stock_analysis, query_competitor_analysis

# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Set up LLM instance
llm = OpenAI(model_name="gpt-4", api_key=openai_api_key)

# Streamlit UI
st.title("Dynamic Stock Analysis with LlamaIndex")

# Report type selection
report_type = st.selectbox("What type of report do you want?", ["Single Stock Outlook", "Competitor Analysis"])

if report_type == "Single Stock Outlook":
    symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, TSLA):")
    if symbol and st.button("Generate Report"):
        with st.spinner(f"Fetching data for {symbol}..."):
            stock_data, error = fetch_stock_data(symbol)
            if error:
                st.error(error)
            else:
                index = create_index_from_stock_data(stock_data, symbol, llm)
                report = query_stock_analysis(index, symbol)
                st.write(report)

elif report_type == "Competitor Analysis":
    symbol1 = st.text_input("Enter First Stock Symbol (e.g., AAPL):")
    symbol2 = st.text_input("Enter Second Stock Symbol (e.g., MSFT):")
    if symbol1 and symbol2 and st.button("Generate Comparative Report"):
        with st.spinner(f"Fetching data for {symbol1} and {symbol2}..."):
            data1, error1 = fetch_stock_data(symbol1)
            data2, error2 = fetch_stock_data(symbol2)

            if error1:
                st.error(f"Error fetching data for {symbol1}: {error1}")
            elif error2:
                st.error(f"Error fetching data for {symbol2}: {error2}")
            else:
                index1 = create_index_from_stock_data(data1, symbol1, llm)
                index2 = create_index_from_stock_data(data2, symbol2, llm)
                report = query_competitor_analysis(index1, symbol1, index2, symbol2)
                st.write(report)
