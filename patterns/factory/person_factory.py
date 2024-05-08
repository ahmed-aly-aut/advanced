from patterns.factory.person import IPerson
from patterns.factory.student import Student
from patterns.factory.teacher import Teacher


class PersonFactory:
    @staticmethod
    def create_person(person_type: str) -> IPerson:
        if person_type == "student":
            return Student()
        elif person_type == "teacher":
            return Teacher()
        else:
            raise ValueError("Invalid person type")
