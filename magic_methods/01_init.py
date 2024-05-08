import time
from typing import Callable


class Rectangle:
     def __init__(self, width: int, height: int) -> None:
         self.width = width
         self.height = height


rectangle = Rectangle(21, 42)
print(rectangle.width)
print(rectangle.height)

