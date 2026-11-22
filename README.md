# Ginko Stock Screener

A basic stock screener built using Python and SQLite.

# About:

A mini project that scans stocks from both the Bombay Stock Exchange (BSE) and New York Stock Exchange (NYSE) to identify promising stocks based on a predefined investment strategy.

# Functions:

- **Ingestion:** Fetches stock market data from BSE and NYSE using the Yahoo Finance Python API (`yfinance`).
- **Filtering:** Filters stocks based on a predefined investment strategy.
- **Selection:** Returns a list of the best stock picks from both markets.
- **Notification:** Emails the selected stocks to the user's email address.

# Limitations:

- The emailing system is incomplete and requires manual intervention.
- The program requires the user to execute each Python script in a specific order.
- The screening strategy uses predefined criteria and does not guarantee profitable investments.

# Implementation Details:

- Written in Python.
- Uses `yfinance` to retrieve stock market data.
- Uses SQLite for database management.
- Separates data ingestion, filtering, and notification into individual scripts.

# How to Use:

Run the following Python scripts in order:

**1. Ingest stock market data:**

```bash
python Ingestion.py
```

**2. Filter stocks based on the predefined strategy:**

```bash
python Filter.py
```

**3. Generate and email the selected stocks:**

```bash
python Notify.py
```

The scripts must be executed in this order for the program to function as intended.
