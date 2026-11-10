# Name Isam Zia Roll no: TRN-2026-00346 


import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()
        elapsed = end - start

        print(f"Execution time: {elapsed:.6f} seconds")

        return result

    return wrapper


def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args}")
        print(f"Keyword arguments: {kwargs}")

        return func(*args, **kwargs)

    return wrapper


@timer
@log_calls
def sum_numbers(limit):
    return sum(range(1, limit + 1))


result = sum_numbers(1_000_000)
print("Sum:", result)
