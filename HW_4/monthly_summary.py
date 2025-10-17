"""Task 4-4: A simple CLI for tracking income and expenses with monthly summary."""
import sqlite3
from typing import Literal
from datetime import datetime

DB_FILE = "finances.db"
FinanceType = Literal["income", "expense"]


def create_finances_table(conn: sqlite3.Connection) -> None:
    """
    Create the 'finances' table if it does not exist.
    """
    conn.execute("""
        CREATE TABLE IF NOT EXISTS finances (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT CHECK(type IN ('income','expense')) NOT NULL,
            purpose TEXT NOT NULL,
            amount REAL NOT NULL,
            time TEXT NOT NULL,
            UNIQUE(type, purpose, amount, time)
        )
    """)


def insert_finance(conn: sqlite3.Connection, f_type: FinanceType, purpose: str,
                   amount: float, time: str) -> None:
    """
    Insert a new transaction into the table.
    """
    try:
        conn.execute(
            "INSERT INTO finances (type, purpose, amount, time) VALUES (?, ?, ?, ?)",
            (f_type, purpose, amount, time)
        )
        print(f"{f_type.capitalize()} added: {purpose}, {amount}, {time}")
    except sqlite3.IntegrityError:
        print(f"Duplicate transaction: {f_type}, {purpose}, {amount}, {time}")


def get_monthly_summary(conn: sqlite3.Connection, year: int, month: int) -> None:
    """
    Calculate total income and expenses for the given month.
    """
    # SQL фильтр по году и месяцу
    month_str = f"{year:04d}-{month:02d}"  # "YYYY-MM"
    cursor = conn.execute("""
        SELECT type, SUM(amount) 
        FROM finances
        WHERE strftime('%Y-%m', time) = ?
        GROUP BY type
    """, (month_str,))

    summary = {"income": 0.0, "expense": 0.0}
    for f_type, total in cursor:
        summary[f_type] = total if total is not None else 0.0

    print(f"\n--- Monthly Summary for {month_str} ---")
    print(f"Total Income : {summary['income']}")
    print(f"Total Expense: {summary['expense']}")
    print(f"Net Balance  : {summary['income'] - summary['expense']}")


def cli_interface() -> None:
    """
    CLI interface for adding transactions and viewing monthly summary.
    """
    with sqlite3.connect(DB_FILE) as conn:
        create_finances_table(conn)

        while True:
            print("\nChoose an action:")
            print("1. Add a transaction")
            print("2. Show monthly summary")
            print("Enter to exit")
            choice = input("Choice: ").strip()

            if choice == "":
                print("Exiting CLI.")
                break

            if choice == "1":
                # Добавление транзакции
                transaction_choice = input(
                    "Type income or expense (enter 1 or 2): ").strip()
                if transaction_choice not in ("1", "2"):
                    print("Invalid type.")
                    continue
                f_type: FinanceType = "income" if transaction_choice == "1" else "expense"

                purpose = input("Purpose: ").strip()
                if purpose == "":
                    print("Purpose cannot be empty.")
                    continue

                try:
                    amount = float(input("Amount: ").strip())
                except ValueError:
                    print("Invalid amount.")
                    continue

                time = input("Time (YYYY-MM-DD HH:MM): ").strip()
                if time == "":
                    print("Time cannot be empty.")
                    continue

                insert_finance(conn, f_type, purpose, amount, time)

            elif choice == "2":
                # Count monthly summary
                try:
                    year = int(input("Enter year (YYYY): ").strip())
                    month = int(input("Enter month (1-12): ").strip())
                    if not 1 <= month <= 12:
                        print("Invalid month.")
                        continue
                except ValueError:
                    print("Invalid input.")
                    continue

                get_monthly_summary(conn, year, month)

            else:
                print("Invalid choice.")


if __name__ == "__main__":
    cli_interface()
