"""Task 4-1: A simple personal expense tracker using SQLite."""
import sqlite3

DB_FILE = "expenses.db"


def create_expenses_table(conn: sqlite3.Connection) -> None:
    """
    Create the 'expenses' table if it does not exist.
    Fields:
        id        - integer primary key
        purpose   - text, description of the expense
        amount    - real, expense amount
        time      - text, timestamp of the expense
    """
    conn.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            purpose TEXT NOT NULL,
            amount REAL NOT NULL,
            time TEXT NOT NULL,
            UNIQUE(purpose, amount, time)

        )
    """)
    print("Table 'expenses' created (if not exists).")


def insert_expense(
        conn: sqlite3.Connection,
        purpose: str,
        amount: float,
        time: str
) -> None:
    """
    Insert a single expense record into the table.
    """
    try:
        conn.execute(
            "INSERT INTO expenses (purpose, amount, time) VALUES (?, ?, ?)",
            (purpose, amount, time)
        )
        print(f"Inserted expense: {purpose}, {amount}, {time}")
    except sqlite3.IntegrityError:
        print("Duplicate expense detected, skipping insert.")


def fetch_expenses(conn: sqlite3.Connection) -> None:
    """
    Fetch and display all expenses from the table.
    """
    cursor = conn.execute("SELECT id, purpose, amount, time FROM expenses")
    print("\n--- All Expenses ---")
    for row in cursor:
        expense_id, purpose, amount, time = row
        print(f"ID: {expense_id}, Purpose: {purpose}, Amount: {amount}, Time: {time}")


if __name__ == "__main__":
    # Use context manager to automatically commit and close the connection
    with sqlite3.connect(DB_FILE) as conn:
        # Create table
        create_expenses_table(conn)

        # Insert example expenses
        insert_expense(conn, "Groceries", 50.75, "2025-10-16 12:30")
        insert_expense(conn, "Transport", 15.20, "2025-10-16 08:00")
        insert_expense(conn, "Coffee", 4.50, "2025-10-16 09:15")


        # Fetch and display all expenses
        fetch_expenses(conn)
