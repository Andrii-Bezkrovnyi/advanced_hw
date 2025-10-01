"""
Task 1-4:
Compare execution time of Fibonacci implementations with different caching strategies.
"""
import time
from functools import lru_cache, wraps


# Decorator to measure execution time
def time_logger(label):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"[{label}] Execution time: {end - start:.6f} seconds")
            return result

        return wrapper

    return decorator


# Without cache
def fib_no_cache(num):
    if num < 2:
        return num
    return fib_no_cache(num - 1) + fib_no_cache(num - 2)


# With custom cache implementation
cache = {}


def fib_custom_cache(num):
    if num in cache:
        return cache[num]
    if num < 2:
        cache[num] = num
    else:
        cache[num] = fib_custom_cache(num - 1) + fib_custom_cache(num - 2)
    return cache[num]


# With functools.lru_cache with maxsize=10
@lru_cache(maxsize=10)
def fib_lru_10(num):
    if num < 2:
        return num
    return fib_lru_10(num - 1) + fib_lru_10(num - 2)


# With functools.lru_cache with maxsize=16
@lru_cache(maxsize=16)
def fib_lru_16(num):
    if num < 2:
        return num
    return fib_lru_16(num - 1) + fib_lru_16(num - 2)


@time_logger("Fibonacci (no cache)")
def run_no_cache():
    return [fib_no_cache(i) for i in range(25)]


@time_logger("Fibonacci (custom cache)")
def run_custom_cache():
    return [fib_custom_cache(i) for i in range(25)]


@time_logger("Fibonacci (lru_cache maxsize=10)")
def run_lru_10():
    return [fib_lru_10(i) for i in range(25)]


@time_logger("Fibonacci (lru_cache maxsize=16)")
def run_lru_16():
    return [fib_lru_16(i) for i in range(25)]


if __name__ == "__main__":
    print(run_no_cache())
    print(run_custom_cache())
    print(run_lru_10())
    print(run_lru_16())
