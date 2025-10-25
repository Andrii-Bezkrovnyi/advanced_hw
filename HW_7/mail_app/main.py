# === Main program ===
import datetime

from HW_7.mail_app.database_app import create_database, search_users, insert_user
from HW_7.mail_app.mail_app import send_email_stub, send_email
from HW_7.mail_app.user_app import User

def input_user_data() -> User:
    """
    Prompts the user to input personal data and returns a User instance.
    """
    print("\nPlease enter user information:")
    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()
    patronymic = input("Patronymic: ").strip()
    email = input("Email: ").strip()
    while True:
        birth_str = input("Birth date (YYYY-MM-DD): ").strip()
        try:
            birth_date = datetime.date.fromisoformat(birth_str)
            break
        except ValueError:
            print("❌ Invalid date format. Please use YYYY-MM-DD.")

    return User(first_name, last_name, patronymic, email, birth_date)

# User registration
def register_user(user: User, test_mode: bool = True):
    """
    Registers a user in the database and sends an email.

    Args:
        user (User): The user to register.
        test_mode (bool): If True, email is not actually sent but printed.
    """
    if not test_mode:
        user = input_user_data()

    insert_user(user)

    if test_mode:
        send_email_stub(user)
    else:
        send_email(user)


if __name__ == "__main__":
    create_database()

    # Example users
    user1 = User("Andrii", "Andriiovych", "Andriiv", "test1@example.com",
                 datetime.date(1998, 5, 14))
    user2 = User("Olena", "Koval", "Mykolayivna", "test2@example.com",
                 datetime.date(2001, 2, 3))

    # Register in test mode (no real email sent)
    register_user(user1, test_mode=True)
    register_user(user2, test_mode=True)

    print("\n--- Searching for 'Andrii' ---")
    found = search_users("Andrii")
    for row in found:
        print(row)

    print("\n--- Now sending real email ---")
    register_user(user1, test_mode=False)
