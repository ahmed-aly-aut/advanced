from patterns.factory.person import IPerson


class Teacher(IPerson):

    def __init__(self) -> None:
        self.name = "Basic Teacher Name"

    @staticmethod
    def person_method() -> None:
        print("I'm a teacher")
