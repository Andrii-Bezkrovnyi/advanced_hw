"""Task 3-1: Create a dictionary, save it to a JSON file, and read it back."""
import json


def create_sample_data() -> dict[str, any]:
    """Create a simple dictionary with sample data."""
    return {
        "name": "Alice",
        "age": 25,
        "is_student": False,
        "skills": ["Python", "Data Analysis", "Machine Learning"],
        "address": {
            "city": "New York",
            "country": "USA"
        }
    }


def save_to_json(data: dict[str, any], filename: str) -> None:
    """Save dictionary data to a JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"Data has been saved to '{filename}'.")


def load_from_json(filename: str) -> dict[str, any]:
    """Load dictionary data from a JSON file."""
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"Data has been loaded from '{filename}'.")
    return data


if __name__ == "__main__":
    file_name = "sample_data.json"

    # Create dictionary
    sample_data = create_sample_data()
    print("Original data:", sample_data)

    # Save dictionary to JSON
    save_to_json(sample_data, file_name)

    # Load JSON from file
    loaded_data = load_from_json(file_name)
    print("Loaded data:", loaded_data)
