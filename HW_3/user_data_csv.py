"""
Task 3-7:
Create a function that generates a CSV file based on the data entered via the console.
The file may contain the following items: names, nicknames, dates of birth and place
of residence. Implement the ability to rewrite a file, add new rows to an explicit file,
 read rows from a file, and convert everything instead of XML and JSON formats
"""
import csv
import json
import xml.etree.ElementTree as ET
from typing import List, Dict

CSV_FILE = "user_data.csv"


def input_user_data() -> Dict[str, str]:
    """
    Prompt user to input a single row of data and return it as a dictionary.
    """
    first_name = input("Enter first name: ").strip()
    last_name = input("Enter last name: ").strip()
    birth_date = input("Enter birth date (YYYY-MM-DD): ").strip()
    city = input("Enter city of residence: ").strip()
    return {
        "first_name": first_name,
        "last_name": last_name,
        "birth_date": birth_date,
        "city": city,
    }


def write_csv(data: List[Dict[str, str]], mode: str = "w") -> None:
    """
    Write data to CSV file. Mode 'w' overwrites, 'a' appends.
    """
    fieldnames = ["first_name", "last_name", "birth_date", "city"]
    with open(CSV_FILE, mode, newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if mode == "w":
            writer.writeheader()
        for row in data:
            writer.writerow(row)
    print(f"Data written to {CSV_FILE} ({'overwrite' if mode == 'w' else 'append'})")


def read_csv() -> List[Dict[str, str]]:
    """
    Read CSV file and return list of dictionaries.
    """
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]


def csv_to_json(data: List[Dict[str, str]]) -> str:
    """
    Convert list of dicts to JSON string.
    """
    return json.dumps(data, indent=4, ensure_ascii=False)


def save_to_json(data: List[Dict[str, str]], filename: str) -> None:
    """
    Save list of dicts to a JSON file.
    """
    with open(filename, "w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile, indent=4, ensure_ascii=False)
    print(f"JSON saved to {filename}")


def csv_to_xml(data: List[Dict[str, str]]) -> ET.Element:
    """
    Convert list of dicts to XML ElementTree.
    """
    root = ET.Element("users")
    for row in data:
        user_elem = ET.SubElement(root, "user")
        for key, value in row.items():
            child = ET.SubElement(user_elem, key)
            child.text = value
    return root


def save_xml(root: ET.Element, filename: str) -> None:
    """
    Save XML ElementTree to file.
    """
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)
    print(f"XML saved to {filename}")


if __name__ == "__main__":
    # Ask user whether to overwrite or append
    action = input("Type 'w' to overwrite CSV or 'a' to append: ").strip().lower()
    num_entries = int(input("How many users to input? "))
    all_data = [input_user_data() for _ in range(num_entries)]
    write_csv(all_data, mode=action)

    # Read CSV
    csv_data = read_csv()
    print("\n--- CSV Data ---")
    for row in csv_data:
        print(row)

    # Convert to JSON
    json_str = csv_to_json(csv_data)
    print("\n--- JSON Data ---")
    print(json_str)
    save_to_json(csv_data, "user_data.json")

    # Convert to XML
    xml_root = csv_to_xml(csv_data)
    save_xml(xml_root, "user_data.xml")
