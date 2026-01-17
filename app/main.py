class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = []
    for item in people:
        person = Person(item["name"], item["age"])
        persons.append(person)
    for item in people:
        person = Person.people[item["name"]]
        if item.get("wife") is not None:
            person.wife = Person.people[item["wife"]]
        if item.get("husband") is not None:
            person.husband = Person.people[item["husband"]]
    return persons
