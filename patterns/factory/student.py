from patterns.factory.person import IPerson


class Student(IPerson):

    def __init__(self) -> None:
        self.name = "Basic Student Name"

    @staticmethod
    def person_method() -> None:
        print("I'm a student")
