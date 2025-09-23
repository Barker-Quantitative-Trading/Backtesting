# Strategy Layer System Design

## 1. Overview
The goal of the strategy layer is to create a structure in which users can effectively create trading strategies which can then be sent to the execution layer for testing or live trading. This layer will evaluate whether algorithms meet coding standards and have all the necessary information for the system to use. This stage is essentially a check, is your strategy a complete working model? Or is there more you need to figure out before you can test it?

** Key Objectives **
- Flexible to accomodate any potential strategy offered by a team or individual
- Maintain integrity of the system for testing
- Save past strategies

## 2. System Architecture
All strategies/algorithms submitted to the strategy layer must clearly outline the following:
- ** What stocks are to be monitored
   - ex. S&P 500 Companies
   - ex. Electrical commodities market
- ** What <u>about</u> the stocks should be monitored
   - ex. A list of technical indicators
   - ex. The average range of prices over a 6 month period
- ** Conditions of a buy signal
   - ex. RSI < 30
   - ex. Price value dips below lowest value in the average range
- ** How much to allocated towards a buy
   - ex. Always allocate 10% of liquid capital
   - ex. Always allocated $500
- ** Exit Strategy
   - This is essentially how long you stay in the buy and when you sell
   - ex. RSI > 70
   - ex. Price comes up to some expected range
- ** Dataset
   - Define what set of data to backtest upon
   - Or indicate live trading
   - ex. 2015-2025 S&P 500 prices

- ** Written Justification
   - Please write a paragraph or two explaining why you are trying this strategy, your hypothesis, and what makes it unique
   - Use .md format


