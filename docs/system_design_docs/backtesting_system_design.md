## Idaho Quantitative Traders Club
# Backtesting System
## Software Design Document

Name: Ibrahim Mansour

Date Created: 09-21-2025

Date Last Updated: 09-21-2025

## Summary

- [1 Introduction](#1-introduction)
- [2 System Overview](#2-system-overview)
- [3 System Architecture](#3-system-architecture)
- [4 Data Design](#4-data-design)
- [5 Component Design](#5-component-design)
- [6 Human Interface Design](#6-human-interface-design)
- [7 Requirements Matrix](#7-requirements-matrix)
- [8 Appendices](#8-appendices)

## 1 Introduction

### 1.1 Purpose

This document defines the overall design of the backtesting system and how it should be built. Those who are trying to get a better picture of how the whole system comes together will benefit from this document greatly.

### 1.2 Scope

The backtesting system is meant to provide as realistic of a testing environment as possible to test trading strategies. To accomplish this task we will simulate trading strategies on historical market data. This allows us to evaluate profitability, risk, accuracy, and robustness **before** moving to live trading.
> **Note:** Backtesting is a vital part of strategy development, but no matter how rigorous, it cannot perfectly predict future performance. Treat backtests as supporting evidence, not guarantees. Real significance comes from live trading validation. Ultimately, most professionals place far greater weight on live trading results than on backtests alone.

### 1.3 Overview

This document will first go over the general system and what it can be used for then explore how the systems pieces will interact and finally look over the tech stack and specific requirements.

### 1.4 Reference Material

Optional. List any documents that were used or would help better explain the choices made in this document.

### 1.5 Definitions and Acronyms

Candle - A candle is a visual representation showing how the price of something moved in a given period. The top is the highest the price moved, and the bottom is the lowest the price moved. The filled in chunk in the middle is the body of the candle. If the body is green than the bottom of the body shows what the price was right at the beginning of the period and the top shows what the prices was at the end of the period. If the body is red than this is reversed for the body.

## 2 System Overview

This system will allow a user to define a trading strategy in the way of determining and coding buy and sell rules. The user should be able to define the period they want to test on, how frequently there rules will be checked (minutes, hours, days, weeks), and the assets they wish to include. 

The execution layer will then take this information and request the needed assets over the given time period from the data layer. 

The data layer has access to a database full of prices and information for many stocks. The data layer has a backend interface for the execution layer to interact with and request information. 

After requesting and receiving information from the data layer the execution layer will take that information and start acting as a brokerage. It will have some method of keeping track of the account value everytime rules are checked, it will "place" trades and show what positions an account has and how much they are worth, and it will keep track of win loss ratios.
  - An example of this process is as follows:
    - The requested period is 5 years, the frequency of checks is every hour and 25 stocks were listed .
    - The execution layer will start off with an arbitraty account balance and every hour it will check to see if any buy or sell took place on any of the stocks that were listed.
    - It will keep track of the balance every hour and be able to return it at the end of the test.
    - If trades did take place it will affect the account balance and active positions list.
    - If a trade was a winner it will add to its wins and if it was a loser it will add to its lossees.
      - This will mean that the execution layer will somehow have to keep track of intitial entrances.

Once the backtest has concluded the execution layer will send all the information to the reporting layer to be displayed. The execution layer will have to perform calculations on the balance to determine many common ratios that reflect performance such as the sharpe and sortino ratio and max drawdown. Lastly the execution layer will create graphs to show things such as balance over the time period.

## 3 System Architecture

### 3.1 Architectural Design

![Design Diagram](images/Screenshot%202025-09-21%20at%202.14.25%E2%80%AFPM.png)

### 3.2 Design Rationale

Discuss the rationale for selecting the architecture described in 3.1 including trade offs and issues considered. This is a good spot to say why certain things fell in your scope and not someone else. Adding things such as why you chose a specific pattern or style is also good.

## 4 Tools & Tech Stack

### 4.1 Tools

Describe all tools that are needed and used in this part of the project. May include references to download anything not in the initial startup.

### 4.2 Tech Stack

This can likely be the same as other SDD's but may differ if you are working on something specific and need another langauge or piece of architecture.

## 5 Requirements Matrix

Describe all requirements that this document meets.
Example:

Requirement 1: A system that can pull data from a database.

Requirement2: A system that can transform data into a format usable by -other- system.

## 6 Appendices

Optional. Appendices may be included, either directly or by reference, to provide supporting details that could aid in the understanding of the Software Design Document.

Based on [Software Design Document (SDD) Template ](https://devlegalsimpli.blob.core.windows.net/pdfseoforms/pdf-20180219t134432z-001/pdf/software-design-document-2.pdf)

And https://gist.github.com/shenhab/15dbb9eb5422c07f497bf17de299b28d