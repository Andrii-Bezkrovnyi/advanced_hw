def calculate_speed(distance_km: float, time_h: float) -> float:
    """
    Calculate the average speed of a car.

    Args:
        distance_km (float): The distance traveled in kilometers.
        time_h (float): The time taken in hours.

    Returns:
        float: The speed in kilometers per hour (km/h).

    Raises:
        ValueError: If time_h <= 0 or distance_km < 0.
    """
    if time_h <= 0:
        raise ValueError("Time must be greater than zero.")
    if distance_km < 0:
        raise ValueError("Distance cannot be negative.")

    return distance_km / time_h
