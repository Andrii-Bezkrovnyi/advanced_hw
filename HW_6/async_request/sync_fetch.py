"""
Synchronous version: fetches multiple URLs using requests
and logs progress into a database (SQLite).
"""

import requests
import sqlite3
import time

DB_FILE = "sync_logs.db"
URLS = [
    "https://example.com",
    "https://httpbin.org/get",
    "https://jsonplaceholder.typicode.com/posts/1",
]


def init_db():
    """Create log table if it doesn't exist."""
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            message TEXT
        )
    """)
    conn.commit()
    conn.close()


def log_message(message: str):
    """Insert a log message into the database."""
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("INSERT INTO logs (timestamp, message) VALUES (?, ?)", (time.ctime(), message))
    conn.commit()
    conn.close()
    print(message)


def fetch(url: str):
    """Fetch a single URL and log progress."""
    log_message(f"Starting request to {url}")
    response = requests.get(url)
    log_message(f"Response from {url} received with status {response.status_code}")


def main():
    init_db()
    start_time = time.perf_counter()

    for url in URLS:
        fetch(url)

    elapsed = time.perf_counter() - start_time
    print(f"\n⏱️ Total execution time (sync): {elapsed:.2f} seconds")


if __name__ == "__main__":
    main()
