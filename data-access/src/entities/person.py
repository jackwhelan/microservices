class Person:
    def __init__(self, name):
        self.__name = name
    
    def greet(self):
        return f"Hi, my name is {self.__name}"
