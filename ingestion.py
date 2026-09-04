#Importing yfinance, sqlite3, pprint (pretty print)
import yfinance as yf
from yfinance import EquityQuery
import sqlite3 as sql
from pprint import pprint 

#Connection to database
db_connection = sql.connect("stocks.db")
cursor = db_connection.cursor()

cursor.execute("pragma foreign_keys = ON;")

cursor.execute("""
create table if not exists symbols (
    symbol TEXT PRIMARY KEY,
    long_name TEXT,
    market_cap INTEGER,
    exchange TEXT
)
""")

cursor.execute("""
create table if not exists filtered_symbols (
    symbol TEXT PRIMARY KEY,
    long_name TEXT,
    exchange TEXT,
    emailed_at TEXT,
    FOREIGN KEY (symbol) REFERENCES symbols(symbol)
)
""")

#Query for Mid to Large cap stocks.
us = EquityQuery('and', [
    EquityQuery('is-in', ['exchange', 'NYQ']),
    EquityQuery('gte', ['intradaymarketcap', 5_000_000_000]),
    EquityQuery('lte', ['fiftytwowkpercentchange', -25])
])

ind = EquityQuery('and', [
    EquityQuery('is-in', ['exchange', 'BSE']),
    EquityQuery('gte', ['intradaymarketcap', 75_000_000_000]),
    EquityQuery('lte', ['fiftytwowkpercentchange', -25])
])

query = EquityQuery('or', [us, ind])

offset = 0

#Add all the stocks with - Symbol, Marketcap (in B) and Percent Change (52 Week).
while True:
    data = yf.screen(query, offset=offset)

    if offset >= data.get('total', 0): #If page past the max, break.
        break

    for __ in data.get('quotes'):
        try:
            #Inserting into the database - symbol, longName, marketCap, exchange.
            cursor.execute("""
            insert or replace into symbols
            (symbol, long_name, market_cap, exchange)
            values (?, ?, ?, ?)
            """, (
                __.get("symbol"),
                __.get("longName"),
                __.get("marketCap") // 1_000_000_000,
                __.get("exchange")
            ))
        except Exception as exception:
            print(exception)
    db_connection.commit() #Commit additions to the table.
    offset += 25

print("Data Ingested!")