#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name):
        self.name = name
        self._name = 1
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and (1 <= len(name) <= 25):
            print(f"{name}")
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
    name = property(get_name, set_name)
guido = Dog("go")
print(guido.name)
guido.name = "asdddddddddsfdsfdsfsddddddd"