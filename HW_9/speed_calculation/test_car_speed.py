from car_speed import calculate_speed


def test_calculate_speed():
    # Normal cases
    assert calculate_speed(100, 2) == 50.0
    assert calculate_speed(150, 3) == 50.0
    assert calculate_speed(0, 2) == 0.0

    # Floating-point values
    assert round(calculate_speed(120.5, 1.5), 2) == 80.33

    # Edge cases (tiny or large numbers)
    assert round(calculate_speed(1, 0.01), 2) == 100.0
    assert round(calculate_speed(10000, 100), 2) == 100.0

    # Invalid inputs (must raise ValueError)
    try:
        calculate_speed(-5, 2)
    except ValueError as e:
        assert str(e) == "Distance cannot be negative."
    else:
        assert False, "Expected ValueError for negative distance"

    try:
        calculate_speed(10, 0)
    except ValueError as e:
        assert str(e) == "Time must be greater than zero."
    else:
        assert False, "Expected ValueError for zero time"

    print("All tests passed successfully!")


if __name__ == "__main__":
    test_calculate_speed()
