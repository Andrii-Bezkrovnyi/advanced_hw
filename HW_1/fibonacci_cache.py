"""Task 1-3: Fibonacci sequence implementations with different caching strategies."""
from functools import lru_cache

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


if __name__ == "__main__":
    print("Fibonacci (no cache):")
    print([fib_no_cache(i) for i in range(25)])

    print("\nFibonacci (custom cache):")
    print([fib_custom_cache(i) for i in range(25)])

    print("\nFibonacci (functools.lru_cache, maxsize=10):")
    print([fib_lru_10(i) for i in range(25)])

    print("\nFibonacci (functools.lru_cache, maxsize=16):")
    print([fib_lru_16(i) for i in range(25)])
