# overwrite on what we already have to be more specific

class Animal:

    def eat(self):
        print("This animal is eating")


class Rabbit(Animal):

    def eat(self):
        print("This rabbit is eating a carrot")


rabbit = Rabbit()
rabbit.eat()
