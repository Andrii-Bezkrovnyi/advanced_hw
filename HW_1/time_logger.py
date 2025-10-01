"""Task 1-2: A decorator that logs the execution time of a function."""
import time
from functools import wraps


def time_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.5f} seconds")
        return result

    return wrapper


@time_logger
def count_numbers():
    """Returns the sum of numbers from 1 to 100000"""
    return sum(i for i in range(1, 100001))


if __name__ == "__main__":
    count_nums = count_numbers()
    print("Result:", count_nums)
