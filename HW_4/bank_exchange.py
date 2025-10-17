"""
Task 4-5:
Fetch USD exchange rate from Monobank API and store it in SQLite DB.
Handles API rate limiting and demonstrates inserting 3 examples.
"""
import sqlite3
import time
from datetime import datetime
from typing import List, Dict

import requests

API_URL = "https://api.monobank.ua/bank/currency"
DB_FILE = "exchange_rates.db"


# Fetch exchange rates from Monobank API
def fetch_exchange_rates() -> List[Dict]:
    """
    Fetch USD exchange rate from Monobank API.
    Returns a list of dictionaries with 'currency_name',
    'dollar_value', 'current_date'.
    """
    while True:
        response = requests.get(API_URL)
        if response.status_code == 429:
            retry_after = int(response.headers.get("Retry-After", 5))
            print(f"Too many requests. Retrying after {retry_after} seconds...")
            time.sleep(retry_after)
            continue
        response.raise_for_status()
        data = response.json()
        rates_list = []

        for item in data:
            if item.get("currencyCodeA") == 840:  # USD
                currency_name = "UAH"
                rate = item.get("rateSell") or item.get("rateCross")
                if rate:
                    rates_list.append({
                        "currency_name": currency_name,
                        "dollar_value": rate,
                        "current_date": datetime.fromtimestamp(item.get("date", 0))
                    })
        return rates_list


# Initialize SQLite table
def create_table(conn: sqlite3.Connection) -> None:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS exchange_rates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            currency_name TEXT NOT NULL,
            dollar_value REAL NOT NULL,
            current_date TEXT NOT NULL
        )
    """)


# Insert a single rate into DB
def insert_rate(conn: sqlite3.Connection, rate: Dict) -> None:
    conn.execute("""
        INSERT INTO exchange_rates (currency_name, dollar_value, current_date)
        VALUES (?, ?, ?)
    """, (rate["currency_name"], rate["dollar_value"],
          rate["current_date"].strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()


# Fetch all rates from DB
def fetch_all(conn: sqlite3.Connection) -> List[Dict]:
    cursor = conn.execute(
        "SELECT id, currency_name, dollar_value, current_date FROM exchange_rates")
    return [{"id": row[0], "currency_name": row[1], "dollar_value": row[2],
             "current_date": row[3]} for row in cursor]


# --- Demo inserting 3 examples ---
def demo_insert_three_examples():
    rates = fetch_exchange_rates()
    if not rates:
        print("No rates fetched.")
        return

    with sqlite3.connect(DB_FILE) as conn:
        create_table(conn)
        print("--- Inserting 3 examples ---")
        for i in range(3):
            insert_rate(conn, rates[0])
            print(f"Inserted {i + 1}: {rates[0]}")
            time.sleep(1)  # avoid hitting rate limit

        all_rates = fetch_all(conn)
        print("\n--- All rates in DB ---")
        for rate in all_rates:
            print(rate)


if __name__ == "__main__":
    demo_insert_three_examples()
