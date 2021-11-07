'''
Placeholder tests to lay down boilerplate architecture.
'''
from src.entities.person import Person

def test_greet_person():
    '''
    Test that the greet method on a Person object will return the expected greeting.
    '''
    person = Person('John Doe')
    assert person.greet() == 'Hi, my name is John Doe'
