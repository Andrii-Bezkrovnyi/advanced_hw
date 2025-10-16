"""Task 3-4: SQLite example with JSON-serialized extra attributes."""
import json
import sqlite3

# Type alias for extra attributes as a list of key-value pairs
MaterialAttributes = list[tuple[str, any]]


def create_table(conn: sqlite3.Connection) -> None:
    """Create the 'materials' table in the database."""
    conn.execute("""
        CREATE TABLE IF NOT EXISTS materials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            weight REAL NOT NULL,
            height REAL NOT NULL,
            extra_attributes TEXT
        )
    """)
    conn.commit()
    print("Table 'materials' created successfully.")


def insert_material(
        conn: sqlite3.Connection,
        weight: float,
        height: float,
        extra: MaterialAttributes
) -> None:
    """Insert a material record with JSON-serialized extra attributes."""
    extra_json = json.dumps(extra)  # Convert list of tuples to JSON string
    conn.execute(
        "INSERT INTO materials (weight, height, extra_attributes) VALUES (?, ?, ?)",
        (weight, height, extra_json)
    )
    conn.commit()
    print(f"Material inserted: weight={weight}, height={height}, extra={extra}")


def fetch_materials(conn: sqlite3.Connection) -> None:
    """Fetch and display all materials, deserializing the extra attributes."""
    cursor = conn.execute("SELECT id, weight, height, extra_attributes FROM materials")
    for row in cursor:
        material_id, weight, height, extra_json = row
        extra: MaterialAttributes = json.loads(extra_json)
        print(f"ID: {material_id}, Weight: {weight}, Height: {height}, Extra: {extra}")


if __name__ == "__main__":
    # Connect to SQLite database using context manager
    with sqlite3.connect("materials.db") as conn:
        # Create table
        create_table(conn)

        # Insert example materials
        insert_material(conn, 12.5, 5.0, [("color", "red"), ("density", 2.3)])
        insert_material(conn, 7.8, 3.5, [("color", "blue"), ("flexibility", "medium")])
        insert_material(conn, 20.0, 10.0, [("color", "green"), ("hardness", "high")])

        # Fetch and display all materials
        print("\n--- Materials in DB ---")
        fetch_materials(conn)
