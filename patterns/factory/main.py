from patterns.factory.person_factory import PersonFactory

if __name__ == '__main__':
    choice = input("Would type of person do you want to create? ")
    person = PersonFactory.create_person(choice)
    person.person_method()
