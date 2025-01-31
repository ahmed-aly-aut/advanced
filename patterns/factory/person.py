from abc import ABCMeta, abstractmethod


class IPerson(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def person_method() -> None:
        """ Interface Method"""
