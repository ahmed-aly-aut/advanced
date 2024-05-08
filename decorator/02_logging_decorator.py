# Practical Example #1 - Logging
import logging
from typing import Callable


def logged[T, ** P](function: Callable[P, T]) -> Callable[P, T]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        logging.info(f"Calling {function.__name__}")
        value = function(*args, **kwargs)
        logging.info(f"Finished calling {function.__name__} and returned value {value}")
        return value

    return wrapper


@logged
def add(x, y):
    return x + y


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info(add(10, 20))
