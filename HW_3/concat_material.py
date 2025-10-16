"""
Task 3-6:
Concatenate multiple fields in a SQLite database using a user-defined function.
"""
import sqlite3


def concat_fields(*args: any) -> str:
    return "".join(str(arg) for arg in args if arg is not None)


def concat_function(db_path: str) -> None:
    with sqlite3.connect(db_path) as conn:
        # Register user-defined function
        conn.create_function("concat_fields", -1, concat_fields)

        # Test query on existing table 'materials'
        cursor = conn.execute(
            "SELECT id, concat_fields(weight, height, extra_attributes) FROM materials"
        )
        for material_id, concatenated in cursor:
            print(f"ID: {material_id} → {concatenated}")


if __name__ == "__main__":
    database_path = "materials.db"
    concat_function(database_path)
