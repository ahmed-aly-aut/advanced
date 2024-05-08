import logging
from collections.abc import Generator


def my_generator(n: int) -> Generator[int, None, None]:
    for x in range(n):
        yield x ** 3


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    values = my_generator(200)
    logging.info(next(values))

    for x in values:
        logging.info(x)
