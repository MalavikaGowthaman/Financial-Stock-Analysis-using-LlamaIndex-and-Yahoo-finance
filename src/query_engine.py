from llama_index.core import VectorStoreIndex

def query_stock_analysis(index, symbol):
    """
    Generate a stock analysis report for a given symbol.
    Args:
        index (VectorStoreIndex): LlamaIndex instance for querying.
        symbol (str): Stock ticker symbol (e.g., AAPL).
    Returns:
        str: Generated report as a string.
    """
    query = f"""
    Write a detailed report on the outlook for {symbol} stock for the next five years.
    Include:
    - Analysis
    - Risks
    - Growth potential
    - Positive and negative impacts
    - Investment advice.
    """
    response = index.as_query_engine().query(query)
    return str(response)


def query_competitor_analysis(index1, symbol1, index2, symbol2):
    """
    Generate a comparative report for two stock symbols.
    Args:
        index1 (VectorStoreIndex): LlamaIndex for the first stock.
        symbol1 (str): First stock symbol.
        index2 (VectorStoreIndex): LlamaIndex for the second stock.
        symbol2 (str): Second stock symbol.
    Returns:
        str: Comparative report as a string.
    """
    query = f"""
    Compare the stocks {symbol1} and {symbol2}. Include:
    - Market performance
    - Competitive advantages
    - Risks and opportunities
    - Investment recommendations.
    """
    response1 = index1.as_query_engine().query(query)
    response2 = index2.as_query_engine().query(query)
    return f"Comparison Report:\n\n{response1}\n\n{response2}"
