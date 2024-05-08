from abc import ABCMeta, abstractmethod


class IPerson(metaclass=ABCMeta):

    @abstractmethod
    def person_method(self) -> None:
        pass


class Person(IPerson):

    def person_method(self) -> None:
        print("I am a person")


class ProxyPerson(IPerson):
    def __init__(self) -> None:
        self.person = Person()

    def person_method(self) -> None:
        print("I am tje proxy functionality")
        self.person.person_method()
