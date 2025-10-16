"""Task 1-7: Currying and partial application in Python."""
from functools import partial


# Normal function
def multiply(a, b):
    return a * b


# Curried version
def curried_multiply(a):
    def inner(b):
        return a * b

    return inner


if __name__ == "__main__":
    # Normal multiplication
    print("Normal multiply:", multiply(3, 4))  # 12

    # Curried multiplication
    mul_by_3 = curried_multiply(3)  # partially apply first argument
    print("Curried multiply (3 * 5):", mul_by_3(5))  # 15

    # Partial application to both arguments at once
    mul_by_3_and_4 = curried_multiply(3)(4)
    print("Curried multiply (3 * 4):", mul_by_3_and_4)  # 12

    # Alternative using functools.partial
    mul_by_10 = partial(multiply, 10)  # fix first argument = 10
    print("Partial (10 * 7):", mul_by_10(7))  # 70
