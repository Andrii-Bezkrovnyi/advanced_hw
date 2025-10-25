import datetime
import sqlite3

from HW_7.mail_app.user_app import User

DB_NAME = "users.db"


# === Database functions ===
def create_database():
    """
    Creates the SQLite database and 'users' table if they do not exist.
    The 'birth_date' is stored as ISO string to be compatible with Python 3.12+.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            patronymic TEXT,
            email TEXT UNIQUE NOT NULL,
            birth_date TEXT
        )
    """)
    conn.commit()
    conn.close()
    print("✅ Database and table ready.")


def insert_user(user: User):
    """
    Inserts a user into the database if the email does not already exist.

    Args:
        user (User): The user to insert.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Check if user already exists
    cursor.execute("SELECT 1 FROM users WHERE email = ?", (user.email,))
    if cursor.fetchone():
        print(f"⚠️ User with email {user.email} already exists. Skipping insert.")
        conn.close()
        return

    cursor.execute("""
        INSERT INTO users (first_name, last_name, patronymic, email, birth_date)
        VALUES (?, ?, ?, ?, ?)
    """, (user.first_name, user.last_name, user.patronymic, user.email,
          user.birth_date.isoformat()))
    conn.commit()
    conn.close()
    print(f"✅ User {user.get_full_name()} added to database.")


def search_users(name_part: str):
    """
    Searches users by first name, last name, or patronymic substring.

    Args:
        name_part (str): Substring to search for.

    Returns:
        List[tuple]: List of tuples containing user data with birth_date as datetime.date.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT first_name, last_name, patronymic, email, birth_date
        FROM users
        WHERE first_name LIKE ? OR last_name LIKE ? OR patronymic LIKE ?
    """, (f"%{name_part}%", f"%{name_part}%", f"%{name_part}%"))
    results = cursor.fetchall()
    conn.close()
    print(f"🔍 Found {len(results)} result(s) for '{name_part}'")

    # Convert birth_date back to datetime.date
    formatted_results = []
    for row in results:
        first_name, last_name, patronymic, email, birth_date_str = row
        birth_date = datetime.date.fromisoformat(birth_date_str)
        formatted_results.append((first_name, last_name, patronymic, email, birth_date))

    return formatted_results
