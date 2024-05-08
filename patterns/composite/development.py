from patterns.composite.department import IDepartment


class Development(IDepartment):
    def __init__(self, employees: int) -> None:
        self.employees = employees

    def print_department(self) -> None:
        print(f"Development Department: {self.employees}")
