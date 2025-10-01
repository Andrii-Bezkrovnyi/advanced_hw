"""Task 1-5: Generate a list of 10 random integers between 1 and 100,"""
import random

# Generate a list of 20 random integers from 1 to 50
numbers = [random.randint(1, 100) for _ in range(10)]
print("Original list:", numbers)

# Get squares of odd numbers
odd_squares = [x ** 2 for x in numbers if x % 2 != 0]
print("Squares of odd numbers:", odd_squares)
