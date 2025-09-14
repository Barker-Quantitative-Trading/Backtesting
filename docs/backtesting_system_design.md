# Backtesting System Design

## 1. Overview
The goal of this backtesting system is to simulate trading strategies on historical market data.  
It allows us to evaluate profitability, risk, accuracy, and robustness **before** moving to live trading.
**Note:** Backtesting is a vital part of strategy development, but no matter how rigorous, it cannot perfectly predict future performance. Treat backtests as supporting evidence, not guarantees. Real significance comes from live trading validation. Ultimately, most professionals place far greater weight on live trading results than on backtests alone.

**Key objectives:**
- Flexible enough to support multiple strategies.
    > **Note:** Buy and sell functions should be independent of strategy. Think only receiving inputs such as ticker, price, shares and then changing internal variables to reflect the trade being placed.
- Modular design for easy contribution and maintenance.
    > **Note:** Be mindful of high coupling, as it reduces modularity and makes strategies harder to maintain.
- Reproducible results across machines and environments.
- Extensible for future live trading integration.

---

## 2. System Architecture
The system is divided into layers:

- **Data Layer**  
  - Loads historical market data from database.
  - Cleans and normalizes data for strategies if necessary.

- **Strategy Layer**  
  - Defines entry/exit rules.
  - Supports plug-and-play strategy modules.

- **Execution Layer**  
  - Simulates order execution.
     > **Note:** In the future be sure to consider that live trading has things like transaction costs, slippage, and volume variations.

- **Portfolio Layer**  
  - Tracks positions.
  - Tracks cash depending on time period of trades (minute, hour, day basis).

- **Reporting Layer**  --**This may be a seperate team**--
  - Generates performance metrics (sharpe, sortino, etc. ratios)
  - Creates plots and reports (equity curve, drawdowns, trade stats).

---

## 3. Data Handling
- **Supported Assets:** equities (initial focus), extendable to crypto, futures, and possibly options.  
- **Input Formats:** Dependent on database
- **Considerations:**  
  - Corporate actions: stock splits, dividends.

---

## 4. Strategy Implementation
- Base interface for creating a strategy.
- Each strategy is a class with methods:
- `generate_signals(data)` → entry/exit signals.
- `risk_and_position_size(data)` → how much to buy/sell based on risk.
    - Could return a percent, number of shares, etc.

**Example pseudocode:**
```python
class MomentumStrategy(Strategy):
  def generate_signals(self, data):
      return data['close'] > FiftyDayMovingAverage
  def risk_and_position_size(self, data): #returns percent of max position
      if 1.04 * data['close'] > FiftyDayMovingAverage:
        return 1
      else:
        return 0.5


