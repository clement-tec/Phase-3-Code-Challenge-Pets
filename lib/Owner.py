from Purchase import Purchase
class Owner:
    def __init__(self, name):
        self._name = name
        self._purchase = []

    def name(self):
        return self._name

    def get_purchase(self):
        return self._purchase

    def set_purchase(self, purchase):
        self._purchase.append(purchase)

    purchase = property(get_purchase, set_purchase)

    def get_animals(self):
        animals_set = set()
        for purchase in self._purchase:
            animals_set.add(purchase.animal)
        return list(animals_set)
    animals = property(get_animals)

    def purchase_animal(self, animal, price, animal_name):
        purchase = Purchase(animal, price, animal_name)
        purchase.owner = self
        self.purchase = purchase

    def all_purchases(self):
        return self._purchase

    def total_purchases(self):
        total = 0
        for purchase in self._purchase:
            total += purchase.price
        return total