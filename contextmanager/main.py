from contextlib import contextmanager
from typing import Literal, TextIO, Iterator

type Mode = Literal["r", "w", "a"]


@contextmanager
def open_managed_file(filename: str, mode: Mode = "r") -> Iterator[TextIO]:
    file: TextIO = open(filename, mode)
    try:
        yield file
    except AttributeError:
        print("Caught Exception")
    finally:
        file.close()


with open_managed_file("notes.txt", "w") as file:
    file.write("Hello, World!")
    file.something()
