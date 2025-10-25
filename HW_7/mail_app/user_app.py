import datetime
from dataclasses import dataclass


@dataclass
class User:
    """
    Data class representing a user.

    Attributes:
        first_name (str): User's first name.
        last_name (str): User's last name.
        patronymic (str): User's patronymic.
        email (str): User's email address.
        birth_date (datetime.date): User's date of birth.
    """

    first_name: str
    last_name: str
    patronymic: str
    email: str
    birth_date: datetime.date

    def get_full_name(self) -> str:
        """
        Returns the full name of the user in the format 'Last First Patronymic'.
        """
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    def get_short_name(self) -> str:
        """
        Returns a short name in the format 'Last F. P.'.
        """
        return f"{self.last_name} {self.first_name[0]}. {self.patronymic[0]}."

    def get_age(self) -> int:
        """
        Calculates and returns the age of the user in years.
        """
        today = datetime.date.today()
        return today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )

    def __str__(self):
        """
        Returns a string representation of the user with full name and birth date.
        """
        return f"{self.get_full_name()}, born {self.birth_date}"

