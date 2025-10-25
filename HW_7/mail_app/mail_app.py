from dotenv import load_dotenv

from HW_7.mail_app.user_app import User

load_dotenv()

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Email functions
def send_email(user: User):
    """
    Sends a real email to the user via SMTP using environment variables.

    Args:
        user (User): The user to send email to.
    """
    sender_email = os.getenv("EMAIL_USER")
    sender_password = os.getenv("EMAIL_PASSWORD")
    smtp_server = os.getenv("MAIL_SENDER_SERVER")

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Registration Confirmation"
    msg["From"] = sender_email
    msg["To"] = user.email

    body = f"""Hello {user.get_full_name()},

Thank you for registering in our system.

Best regards,
Admin
"""
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(smtp_server, 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, user.email, msg.as_string())
        print(f"📨 Email sent successfully to {user.email}")
    except Exception as e:
        print(f"❌ Error sending email: {e}")


def send_email_stub(user: User):
    """
    Prints a simulated email to the console for test purposes.

    Args:
        user (User): The user to simulate sending email to.
    """
    print(f"🧪 [TEST MODE] Email to {user.email}:")
    print("---")
    print(f"Hello {user.get_full_name()},\n")
    print("Thank you for registering in our system.\n")
    print("Best regards,\nAdmin")
    print("---")
