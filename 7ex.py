class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name, age, adress):
        self.name = name
        self.age = age
        self.adress = adress


    def info(self):
        return {"name": owner.name, "age": owner.age, "adress": owner.adress}


class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner):
        self.breed = breed
        self.owner = owner
        super().__init__(nickname, weight)

    def say(self):
        return "Woof"

    def who_is_owner(self):
        return owner.info()


owner = Owner("Sasha", 17, "Пироговського 18")
owner.info()
dog = Dog("Barbos", 23, "labrador", owner)
print(owner.info())
print(dog.who_is_owner())