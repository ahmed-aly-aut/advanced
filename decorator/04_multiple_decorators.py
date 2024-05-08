# Practical Example #2 Timing
import functools
import logging
import time
from typing import Callable, Any


def benchmark[T, **P](function: Callable[P, T]) -> Callable[P, T]:
    @functools.wraps(function)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        logging.info(f"{function.__name__} took {after - before} seconds to execute!")
        return value

    return wrapper


def logged[T, **P](function: Callable[P, T]) -> Callable[P, T]:
    @functools.wraps(function)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        logging.info(f"Calling {function.__name__}")
        value = function(*args, **kwargs)
        logging.info(f"Finished calling {function.__name__} and returned value {value}")
        return value

    return wrapper


@logged
@benchmark
def myfunction(x):
    result = 1
    for i in range(1, x):
        result = i
    return result


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    myfunction(20000)
