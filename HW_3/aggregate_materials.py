"""Task 3-5: Calculate the rounded average weight of materials in a SQLite database"""
import sqlite3


class AvgWeight:
    """Custom aggregate function to calculate average weight and round
     to nearest integer.
     """

    def __init__(self) -> None:
        self.total: float = 0.0
        self.count: int = 0

    def step(self, value: float) -> None:
        """Add the weight value to the total and increment the count."""
        if value is not None:
            self.total += value
            self.count += 1

    def finalize(self) -> any:
        """Return the rounded average weight or None if no values."""
        if self.count == 0:
            return None
        return round(self.total / self.count, 2)


def calculate_average_weight(db_path: str) -> None:
    """Connect to SQLite DB, register custom aggregate, and calculate average weight."""
    with sqlite3.connect(db_path) as conn:
        # Register custom aggregate function
        conn.create_aggregate("avg_weight", 1, AvgWeight)

        cursor = conn.execute(
            "SELECT avg_weight(weight) FROM materials"
        )
        result = cursor.fetchone()[0]

        print(f"Rounded average weight of all materials: {result}")


if __name__ == "__main__":
    database_path = "materials.db"
    calculate_average_weight(database_path)
