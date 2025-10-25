"""Task 8-5: Stable BMI Calculator with validation and tests"""

def calculate_bmi(height_cm: float, weight_kg: float) -> str:
    """
    Calculate Body Mass Index (BMI) with full input validation.

    Args:
        height_cm (float): Height in centimeters.
        weight_kg (float): Weight in kilograms.

    Returns:
        str: Text message with BMI value and status.

    Raises:
        ValueError: If height_cm or weight_kg are invalid.
    """
    # Validate input types
    if not isinstance(height_cm, (int, float)) or not isinstance(weight_kg, (int, float)):
        raise ValueError("Height and weight must be numeric values.")

    # Validate values
    if height_cm <= 0 or weight_kg <= 0:
        raise ValueError("Height and weight must be positive numbers.")

    # Calculate BMI
    bmi = weight_kg / ((height_cm / 100) ** 2)

    # Determine status
    if bmi < 18.5:
        return f"Your BMI: {bmi:.2f} – underweight."
    elif bmi <= 24.9:
        return f"Your BMI: {bmi:.2f} – weight is normal."
    else:
        return f"Your BMI: {bmi:.2f} – watch your figure."


if __name__ == "__main__":
    # Simple interactive mode
    while True:
        height_input = input("Enter height in cm (or 'off' to exit): ")
        if height_input.lower() == "off":
            print("Exiting the program...")
            break

        weight_input = input("Enter weight in kg (or 'off' to exit): ")
        if weight_input.lower() == "off":
            print("Exiting the program...")
            break

        try:
            height = float(height_input)
            weight = float(weight_input)
            print(calculate_bmi(height, weight))
        except ValueError as e:
            print(f"❌ Error: {e}")
