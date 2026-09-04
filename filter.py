#Importing yfinance, sqlite3, pprint (pretty print), datetime
from yfinance import Ticker
import sqlite3
from pprint import pprint 
from datetime import datetime, timezone

db_connection = sqlite3.connect("stocks.db")
cursor = db_connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")
cursor.execute("select * from symbols order by symbol asc")

stocks = cursor.fetchall()

#Checking if the company has consistently growing profits and revenues
for stock in stocks:
    accept = True

    finances = Ticker(stock[0]).get_income_stmt(as_dict=True, freq="yearly")
    years = [year for year in finances]

    try:
        no_of_years = len(years)-1

        if no_of_years >= 3:
            start_rev = finances[years[no_of_years]].get("TotalRevenue")
            start_inc = finances[years[no_of_years]].get("NetIncome")

            for index in range(no_of_years-1, -1, -1):
                curr_rev = finances[years[index]].get("TotalRevenue")
                curr_inc = finances[years[index]].get("NetIncome")

                if curr_rev > start_rev and curr_inc > start_inc:
                    start_rev = curr_rev
                    start_inc = curr_inc
                else:
                    accept = False
                    break
            
            if accept:
                cursor.execute("""
                insert or replace into filtered_symbols
                (symbol, long_name, exchange, emailed_at)
                values (?, ?, ?, null)""", (stock[0], 
                                        stock[1], 
                                        stock[3]))
                
        else:
            continue
    except:
        continue

db_connection.commit()

print("Data filtered!")