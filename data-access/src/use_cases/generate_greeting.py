from src.entities.person import Person

def greet_person(name: str):
    person = Person(name)
    return person.greet()
