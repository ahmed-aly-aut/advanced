from typing import Self


class Person:
    species: str = "Home sapiens"

    @classmethod
    def get_species(cls) -> str:
        return cls.species


print(Person.get_species())
