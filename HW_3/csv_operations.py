"""Task 3-3: CSV File Operations with Custom Dialect"""
import csv

# Create a custom CSV dialect
csv.register_dialect(
    "my_dialect",
    delimiter=";",  # Use semicolon as separator
    quotechar='"',  # Quote character
    quoting=csv.QUOTE_ALL,  # Quote all fields
    lineterminator="\n",  # New line for each row
)


def write_csv_file(filename: str, data: list[dict[str, str]]) -> None:
    """Write data to a CSV file using the custom dialect."""
    if not data:
        return

    fieldnames = list(data[0].keys())
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, dialect="my_dialect")
        writer.writeheader()
        writer.writerows(data)
    print(f"Data written to '{filename}' using custom dialect.")


def read_csv_file(filename: str) -> list[dict[str, str]]:
    """Read data from a CSV file using the custom dialect."""
    with open(filename, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, dialect="my_dialect")
        data = [row for row in reader]
    print(f"Data read from '{filename}':")
    return data


if __name__ == "__main__":
    file_name = "students.csv"

    # Sample data
    students: list[dict[str, str]] = [
        {"name": "Alice", "age": "25", "faculty": "Engineering"},
        {"name": "Bob", "age": "22", "faculty": "Science"},
        {"name": "Charlie", "age": "23", "faculty": "Mathematics"},
    ]

    # Write CSV
    write_csv_file(file_name, students)

    # Read CSV
    loaded_students = read_csv_file(file_name)
    for student in loaded_students:
        print("Student data: ", student)
