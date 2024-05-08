from abc import ABCMeta, abstractmethod


class IDepartment(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, employees: int) -> None:
        """
        Implement in child class
        :param employees:
        """
        self.employees = None

    @abstractmethod
    def print_department(self) -> None:
        """
        Implement in childclass
        :return:
        """
