class Math:
    @staticmethod
    def add(x: int | float, y: int | float) -> int | float:
        return x + y

    @staticmethod
    def multiply(x: int | float, y: int | float) -> int | float:
        return x * y


print(Math.add(1, 2))
print(Math.multiply(3, 2))
