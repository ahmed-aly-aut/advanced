import logging
from typing import Callable


def my_decorator[T, ** P](function: Callable[P, T]) -> Callable[P, T]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        logging.info("I am decorating your function!")
        return_value = function(*args, **kwargs)
        return return_value

    return wrapper


@my_decorator
def hello(person):
    logging.info(f"Hello {person}")
    return f"Hello {person}!"


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info(hello("Mike"))
