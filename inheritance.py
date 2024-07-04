class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class rabit(Animal):
    def run(self):
        print("This rabbit is runnimg")
class fish(Animal):
    def swim(self):
        print("This fish is swimming")
class hawk(Animal):
    def fly(self):
        print("This hawk is flying")

rabit = rabit()
fish = fish()
hawk = hawk()

#print(rabit.alive)
#fish.eat()
#hawk.sleep()

rabit.run()
fish.swim()
hawk.fly()