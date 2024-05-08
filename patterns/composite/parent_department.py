from patterns.composite.department import IDepartment


class ParentDepartment(IDepartment):

    def __init__(self, employees: int) -> None:
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []

    def add(self, dept: IDepartment) -> None:
        self.sub_depts.append(dept)
        self.employees += dept.employees

    def remove(self, dept: IDepartment) -> None:
        self.sub_depts.remove(dept)
        self.employees -= dept.employees

    def print_department(self) -> None:
        print("Parent Department")
        print(f"Parent Department Base Employees: {self.base_employees}")
        for dept in self.sub_depts:
            dept.print_department()
        print(f"Total number of employees: {self.employees}")
