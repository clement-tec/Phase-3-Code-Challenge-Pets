from .Owner import Owner
from .Animal import Animal

class Purchase:
    
    def __init__(self, owner, animal, price, animal_name):
        if not isinstance(owner, Owner):
            raise TypeError("owner must be an Owner object")
        if not isinstance(animal, Animal):
            raise TypeError("animal must be an Animal object")
        self._owner = owner
        self._animal = animal
        self._price = price
        self._animal_name = animal_name

    def get_price(self):
        return self._price
    price = property(get_price)

    def get_animal_name(self):
        return self._animal_name
    def set_animal_name(self, animal_name):
        self._animal_name = animal_name
    animal_name = property(get_animal_name, set_animal_name)

    def get_owner(self):
        return self._owner
    owner = property(get_owner)

    def get_animal(self):
        return self._animal
    animal = property(get_animal)

    