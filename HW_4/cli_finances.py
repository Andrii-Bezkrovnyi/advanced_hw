"""
Task 4-3:
A simple CLI to manage personal finances using SQLite.
Users can add income and expense records, which are stored in a SQLite database.
"""
import sqlite3
from typing import Literal

DB_FILE = "finances.db"
FinanceType = Literal["income", "expense"]


def create_finances_table(conn: sqlite3.Connection) -> None:
    """
    Create the 'finances' table if it does not exist.
    Fields:
        id     - integer primary key
        type   - 'income' or 'expense'
        purpose- text, description of the transaction
        amount - real, transaction amount
        time   - text, timestamp
    """
    conn.execute("""
        CREATE TABLE IF NOT EXISTS finances (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT CHECK(type IN ('income','expense')) NOT NULL,
            purpose TEXT NOT NULL,
            amount REAL NOT NULL,
            time TEXT NOT NULL,
            UNIQUE(type, purpose, amount, time) -- prevent duplicates
        )
    """)
    print("Table 'finances' created (if not exists).")


def insert_finance(conn: sqlite3.Connection, f_type: FinanceType, purpose: str,
                   amount: float, time: str) -> None:
    """
    Insert a transaction into the table if it does not already exist.
    """
    try:
        conn.execute(
            "INSERT INTO finances (type, purpose, amount, time) VALUES (?, ?, ?, ?)",
            (f_type, purpose, amount, time)
        )
        print(f"{f_type.capitalize()} added: {purpose}, {amount}, {time}")
    except sqlite3.IntegrityError:
        print(f"Duplicate transaction detected: {f_type}, {purpose}, {amount}, {time}")


def fetch_finances(conn: sqlite3.Connection) -> None:
    """
    Fetch and display all transactions from the table.
    """
    cursor = conn.execute("SELECT id, type, purpose, amount, time FROM finances")
    print("\n--- All Transactions ---")
    for row in cursor:
        fid, f_type, purpose, amount, time = row
        print(
            f"ID: {fid}, Type: {f_type}, Purpose: {purpose}, Amount: {amount}, Time: {time}")


def cli_interface() -> None:
    """
    CLI interface to add transactions (income or expense) to the database.
    """
    with sqlite3.connect(DB_FILE) as conn:
        create_finances_table(conn)

        while True:
            print("\nEnter a new transaction (or leave 'type' empty to exit):")
            transaction_type_input = input(
                "Type income or expense (enter 1 or 2): ").strip().lower()
            if transaction_type_input == "":
                print("Exiting CLI.")
                break
            if transaction_type_input not in ("1", "2"):
                print("Invalid type, must be 'income' or 'expense'.")
                continue

            transaction_type: FinanceType = "income" if transaction_type_input == "1" else "expense"

            purpose = input("Purpose: ").strip()
            if purpose == "":
                print("Purpose cannot be empty.")
                continue

            try:
                amount_str = input("Amount: ").strip()
                amount = float(amount_str)
            except ValueError:
                print("Invalid amount, please enter a number.")
                continue

            time = input("Time (YYYY-MM-DD HH:MM): ").strip()
            if time == "":
                print("Time cannot be empty.")
                continue

            insert_finance(conn, transaction_type, purpose, amount, time)

        fetch_finances(conn)


if __name__ == "__main__":
    cli_interface()
