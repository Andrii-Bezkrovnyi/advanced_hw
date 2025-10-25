"""Task 9-3: Student class with validation."""

class Student:
    """Represents a student with personal and academic information."""

    def __init__(self, first_name: str, last_name: str, age: int, average_grade: float):
        if not first_name or not isinstance(first_name, str):
            raise ValueError("First name must be a non-empty string.")
        if not last_name or not isinstance(last_name, str):
            raise ValueError("Last name must be a non-empty string.")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")
        if not isinstance(average_grade, (int, float)) or not (0 <= average_grade <= 100):
            raise ValueError("Average grade must be a number between 0 and 100.")

        self.first_name = first_name.strip().title()
        self.last_name = last_name.strip().title()
        self.age = age
        self.average_grade = float(average_grade)

    def __repr__(self):
        return f"Student({self.first_name} {self.last_name}, {self.age} y.o., grade={self.average_grade:.2f})"

    def is_honors(self) -> bool:
        """Return True if the student's average grade >= 90."""
        return self.average_grade >= 90


if __name__ == "__main__":
    # Create a list of 10 students
    students = [
        Student("Andrii", "Bezkrovnyi", 22, 91.5),
        Student("Olena", "Koval", 20, 78.0),
        Student("Ivan", "Petrenko", 19, 85.3),
        Student("Sofiia", "Melnyk", 21, 95.0),
        Student("Oleh", "Tkachenko", 23, 70.2),
        Student("Maria", "Bondar", 22, 88.7),
        Student("Kateryna", "Lytvyn", 20, 100.0),
        Student("Dmytro", "Shevchenko", 24, 65.0),
        Student("Anna", "Polishchuk", 18, 80.0),
        Student("Vladyslav", "Hrytsenko", 19, 90.0),
    ]

    for s in students:
        print(s)
