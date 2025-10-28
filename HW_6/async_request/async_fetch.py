"""
Asynchronous version: fetches multiple URLs using aiohttp
and logs progress into a database (SQLite).
"""

import aiohttp
import asyncio
import sqlite3
import time

DB_FILE = "async_logs.db"
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


async def fetch(session, url):
    """Fetch a single URL asynchronously and log progress."""
    log_message(f"Starting request to {url}")
    async with session.get(url) as response:
        log_message(f"Response from {url} received with status {response.status}")


async def main():
    init_db()
    start_time = time.perf_counter()

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in URLS]
        await asyncio.gather(*tasks)

    elapsed = time.perf_counter() - start_time
    print(f"\n⏱️ Total execution time (async): {elapsed:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
