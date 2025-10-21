"""
Task 5-1:
Compare performance of threading.
Thread vs ThreadPoolExecutor for factorial computation.
"""
import math
import threading
import time
from concurrent.futures import ThreadPoolExecutor


# Function to compute factorial
def compute_factorial(n: int) -> int:
    return math.factorial(n)


# Function to run tasks using Thread
def run_with_threads(nums):
    threads = []
    start = time.time()
    for num in nums:
        t = threading.Thread(target=compute_factorial, args=(num,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    end = time.time()
    return end - start


# Function to run tasks using ThreadPoolExecutor
def run_with_threadpool(nums):
    start = time.time()
    with ThreadPoolExecutor() as executor:
        executor.map(compute_factorial, nums)
    end = time.time()
    return end - start


if __name__ == "__main__":
    # Sample factorial numbers (small to large)
    numbers = [50000, 60000, 70000, 80000, 90000, 100000]

    print("Running factorial computations...\n")

    t1 = run_with_threads(numbers)
    print(f"Time with Thread: {t1:.4f} seconds")

    t2 = run_with_threadpool(numbers)
    print(f"Time with ThreadPoolExecutor: {t2:.4f} seconds")

    if t2 < t1:
        print("ThreadPoolExecutor is faster.")
    else:
        print("Threads are faster or equal.")
