from data.services.fetch_tiingo import fetch_candle, fetch_asset

def test_fetch_candle_without_end_date():
    """Tests fetching a candle with only a start date."""
    result = fetch_candle("AAPL", "2025/8/01")
    assert isinstance(result, list)
    # Add more specific assertions based on expected API response

def test_fetch_candle_with_end_date():
    """Tests fetching a candle with a start and end date."""
    result = fetch_candle("AAPL", "2020/10/01", "2020/10/02")
    assert isinstance(result, list)
    # Add more specific assertions

def test_fetch_asset():
    """Tests fetching asset metadata."""
    result = fetch_asset("AAPL")
    assert isinstance(result, dict)
    assert result.get("ticker") == "AAPL"
