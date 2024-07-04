class organism:
    alive = True

class animal(organism):
    def eat(self):
        print("This animal is eating")

class dog(animal):
    def bark(self):
        print("This dog is barking")

dog = dog()
animal = animal()

print(dog.alive)
dog.eat()
dog.bark()

#incase of multiple inheritance -----class dog(animal,organism)