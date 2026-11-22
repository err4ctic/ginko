#Ginko Stock Screener
A basic stock screener built using Python and SQLite.

#About:
A basic stock screener that scans both BSE and NYSE to find the best stocks according to a predefined strategy.

#Functions:
- Ingests data using the yahoo finance python api (yfinance) from both BSE and NYSE.
- Filters the stocks based on a predefined strategy.
- Returns a list of the best stock picks from both the markets.
- Emails the stock picks to the user's email.

#Limitations:
The emailing system is half-baked, and requires user intervention.
Along with the program relying on the user to run each file in a fixed order to achieve ideal results.

#Use:
Run the files in the following order:
- Ingestion.py
- Filter.py
- Notify.py
