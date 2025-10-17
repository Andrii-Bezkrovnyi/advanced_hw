"""Task 4-2: A simple CLI tool to manage personal expenses using SQLite."""
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
            UNIQUE(purpose, amount, time)  -- prevent duplicates
        )
    """)
    print("Table 'expenses' created (if not exists).")


def insert_expense(conn: sqlite3.Connection, purpose: str, amount: float,
                   time: str) -> None:
    """
    Insert a single expense into the table if it does not already exist.
    """
    try:
        conn.execute(
            "INSERT INTO expenses (purpose, amount, time) VALUES (?, ?, ?)",
            (purpose, amount, time)
        )
        print(f"Expense added: {purpose}, {amount}, {time}")
    except sqlite3.IntegrityError:
        print(f"Duplicate expense detected: {purpose}, {amount}, {time}")


def fetch_expenses(conn: sqlite3.Connection) -> None:
    """
    Fetch and display all expenses from the table.
    """
    cursor = conn.execute("SELECT id, purpose, amount, time FROM expenses")
    print("\n--- All Expenses ---")
    for row in cursor:
        expense_id, purpose, amount, time = row
        print(f"ID: {expense_id}, Purpose: {purpose}, Amount: {amount}, Time: {time}")


def cli_interface() -> None:
    """
    Simple CLI interface to add expenses to the database.
    """
    with sqlite3.connect(DB_FILE) as conn:
        create_expenses_table(conn)

        while True:
            print("\nEnter a new expense (or leave empty to exit):")
            purpose = input("Purpose: ").strip()
            if purpose == "":
                print("Exiting CLI.")
                break

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

            # Insert the expense
            insert_expense(conn, purpose, amount, time)

        # Show all expenses at the end
        fetch_expenses(conn)


if __name__ == "__main__":
    cli_interface()
