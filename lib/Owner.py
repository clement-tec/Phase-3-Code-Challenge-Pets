from Purchase import Purchase

class Owner:
    def __init__(self, name):
        self._name = name
        self._purchases = []

    def name(self):
        return self._name

    def get_purchases(self):
        return self._purchases

    def set_purchases(self, purchase):
        self._purchases.append(purchase)

    purchases = property(get_purchases, set_purchases)

    def get_animals(self):
        animals_set = set()
        for purchase in self._purchases:
            animals_set.add(purchase.animal)
        return list(animals_set)

    animals = property(get_animals)

    def purchase_animal(self, animal, price, animal_name):
        purchase = Purchase(animal, price, animal_name)
        purchase.owner = self
        self.purchases = purchase

    def all_purchases(self):
        return self._purchases

    def total_purchases(self):
        total = 0
        for purchase in self._purchases:
            total += purchase.price
        return total
