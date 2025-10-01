"""Task 1-6: Fibonacci generator with even number filter using decorators"""
from functools import wraps

# Decorator to keep only even numbers from a generator
def even_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for value in func(*args, **kwargs):
            if value % 2 == 0:
                yield value
    return wrapper


# Fibonacci generator
@even_only
def fibonacci(nums):
    """Generate first n Fibonacci numbers"""
    a, b = 0, 1
    for _ in range(nums):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    print("Even Fibonacci numbers:")
    print(list(fibonacci(20)))  # get first 20 Fibonacci numbers, only even will stay
