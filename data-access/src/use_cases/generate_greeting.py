'''
Placeholder module to lay down boilerplate architecture.
'''
from src.entities.person import Person

def greet_person(name: str):
    '''
    Placeholder function to lay down boilerplate architecture.
    '''
    person = Person(name)
    return person.greet()
