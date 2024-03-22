class Animal:
    amount_of_animals = 0
    def __init__(self, name, color, number_of_legs = None):
        self.name = name
        self.color = color
        self.number_of_legs = number_of_legs
        Animal.amount_of_animals += 1
    
    @classmethod
    def amount_of_animal(cls):
        return f"This is animal class. Currently there is {Animal.amount_of_animals} animals defined"
    
    def description(self):
        return f"Class: {self.__class__.__name__} Type: {str(type(self))} Name: {self.name}, Color: {self.color}, Number of Legs: {self.number_of_legs}"
    


class Mammal(Animal):
    amount_of_mammals = 0
    def __init__(self, name, color, number_of_legs = -1):
        super().__init__(name, color, number_of_legs)
        Mammal.amount_of_mammals += 1
    
    @classmethod
    def amount_of_mammal(cls):
        return f"This is mammal class. Currently there is {Mammal.amount_of_mammals} mammals defined"
    

class Bird(Animal):
    amount_of_birds = 0
    def __init__(self, name, color):
        super().__init__(name, color, 2)
        Bird.amount_of_birds += 1
    
    @classmethod
    def amount_of_bird(cls):
        return f"This is bird class. Currently there is {Bird.amount_of_birds} birds defined"
    
class Fish(Animal):
    amount_of_fish = 0
    def __init__(self, name, color):
        super().__init__(name, color, 0)
        Fish.amount_of_fish += 1
    
    @classmethod
    def amount_of_fish(cls):
        return f"This is fish class. Currently there is {Fish.amount_of_fish} fish defined"

class Dog(Mammal):
    amount_of_dogs = 0
    def __init__(self, name, color):
        super().__init__(name, color, 4)
        Dog.amount_of_dogs += 1
    
    @classmethod
    def amount_of_dog(cls):
        return f"This is dog class. Currently there is {Dog.amount_of_dogs} dogs defined.\nCurrently there is {Animal.amount_of_animals} animals defined."
    


class Cat(Mammal):
    amount_of_cats = 0
    def __init__(self, name, color):
        super().__init__(name, color, 4)
        Cat.amount_of_cats += 1

    @classmethod
    def amount_of_cat(cls):
        return f"This is cat class. Currently there is {Cat.amount_of_cats} cats defined"

cat = Cat("Kitty", "White")
cat2 = Cat("Kitty2", "Black")
print(cat.description())
print(Cat.amount_of_cat())
