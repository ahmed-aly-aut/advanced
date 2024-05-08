import functools
import time
from typing import Callable


def timer[**P, T](function: Callable[P, T]) -> Callable[P, T]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print(f"Function {function.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
@functools.cache
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# 1, 1, 2, 3, 5, 8,...

# with cache 0.0002 seconds
# without cache 18 seconds
print(fibonacci(30))
