from patterns.proxy.person import Person, ProxyPerson

if __name__ == "main":
    p1 = Person()
    p1.person_method()

    p2 = ProxyPerson()
    p2.person_method()
