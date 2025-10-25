"""
Task 7-1:
Function that converts a list of integers into a list of strings.
Includes type annotations.
"""


def convert_int_list_to_str(int_list: list[int]) -> list[str]:
    """
    Convert a list of integers to a list of string values.

    Args:
        int_list (list[int]): List of integers.

    Returns:
        list[str]: List of strings representing the input integers.
    """
    return [str(num) for num in int_list]


if __name__ == "__main__":
    numbers = [1, 2, 3, 42, 100]
    string_numbers = convert_int_list_to_str(numbers)
    print("Original list:", numbers)
    print("Converted list:", string_numbers)
