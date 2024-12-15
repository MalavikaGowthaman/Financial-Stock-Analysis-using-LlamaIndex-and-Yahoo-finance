from llama_index.core import VectorStoreIndex
from llama_index.core import Document
import pandas as pd

def create_index_from_stock_data(stock_data, symbol, llm):
    """
    Create a LlamaIndex from stock data.
    Args:
        stock_data (pd.DataFrame): Stock data as a Pandas DataFrame.
        symbol (str): Stock ticker symbol (e.g., AAPL).
        llm: LLM instance (e.g., OpenAI GPT-4).
    Returns:
        VectorStoreIndex: LlamaIndex instance for querying.
    """
    # Validate stock_data is a DataFrame
    if not isinstance(stock_data, pd.DataFrame):
        raise ValueError("stock_data must be a Pandas DataFrame.")
    
    # Ensure required columns exist
    required_columns = ['High', 'Low', 'Close']
    for col in required_columns:
        if col not in stock_data.columns:
            raise ValueError(f"Missing required column: {col}")

    # Ensure columns are numeric
    stock_data['High'] = pd.to_numeric(stock_data['High'], errors='coerce')
    stock_data['Low'] = pd.to_numeric(stock_data['Low'], errors='coerce')
    stock_data['Close'] = pd.to_numeric(stock_data['Close'], errors='coerce')

    # Drop rows with missing values after conversion
    stock_data = stock_data.dropna(subset=required_columns)

    # Generate a summary of the stock data
    summary = f"Stock Analysis for {symbol}\n"
    summary += f"Highest Price: {stock_data['High'].max():.2f}\n"
    summary += f"Lowest Price: {stock_data['Low'].min():.2f}\n"
    summary += f"Average Closing Price: {stock_data['Close'].mean():.2f}\n\n"
    summary += "Recent Data:\n"
    summary += stock_data.tail(5).to_string(index=False)

    # Create a Document from the summary
    document = Document(text=summary)

    # Create a VectorStoreIndex from the document
    index = VectorStoreIndex.from_documents([document], llm=llm)
    return index
