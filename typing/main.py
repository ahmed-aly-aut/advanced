from typing import TypedDict, Unpack


class Item(TypedDict):
    name: str
    value: float


def info(name: str, **kwargs: Unpack[Item]) -> None:
    print(name, kwargs, sep=": ")


if __name__ == '__main__':
    info("bla", name="Pencil", value=0.1)
