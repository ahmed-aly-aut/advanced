class Circle:
    def __init__(self, radius: int) -> None:
        self.__radius = radius

    @property
    def radius(self) -> int:
        return self.__radius

    @radius.setter
    def radius(self, value: int) -> None:
        if value >= 0:
            self.__radius = value
        else:
            raise ValueError("Radius must be positive")

    @radius.deleter
    def radius(self) -> None:
        print("deleted")
        del self.__radius

    @property
    def diameter(self):
        return self.__radius * 2

c = Circle(5)
print(c.radius)
print(c.diameter)
c.radius = 10
print(c.radius)
print(c.diameter)
del c.radius
