from types import TracebackType
from typing import Literal, TextIO

type Mode = Literal["r", "w", "a"]


class ManagedFile:
    def __init__(self, filename: str, mode: Mode = "r") -> None:
        self.filename = filename
        self.mode = mode
        self.file: TextIO | None = None

    def __enter__(self) -> TextIO:
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool | None:
        if self.file:
            self.file.close()
        if exc_type:
            print("Exception has been handled")
            return True
        return None


with ManagedFile("notes.txt", "w") as file:
    file.write("some todo...")
