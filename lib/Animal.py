class Animal:
    def __init__(self, name, animal_type):
        self._name = name
        self._type = animal_type
        self._purchases = []

    def get_name(self):
        return self._name
    name = property(get_name)

    def get_type(self):
        return self._type
    type = property(get_type)

    def get_owners(self):
        unique_owners = set()
        for purchase in self._purchases:
            unique_owners.add(purchase.owner)
        return list(unique_owners)
    owners = property(get_owners)

    def animal_names(self):
        all_animals = []
        for purchase in self._purchases:
            all_animals.append(purchase.animal_name)
        return all_animals

    def biggest_enthusiast(self):
        if not self._purchases:
            return None

        purchase_counts = {}
        for purchase in self._purchases:
            owner = purchase.owner
            purchase_counts[owner] = purchase_counts.get(owner, 0) + 1

        return max(purchase_counts, key=purchase_counts.get).name()
