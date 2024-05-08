from patterns.composite.accounting import Accounting
from patterns.composite.development import Development
from patterns.composite.parent_department import ParentDepartment

if __name__ == "__main__":
    dept1 = Accounting(200)
    dept2 = Development(170)

    parent_dept = ParentDepartment(30)
    parent_dept.add(dept1)
    parent_dept.add(dept2)

    parent_dept.print_department()

    parent_dept.remove(dept2)

    parent_dept.print_department()

