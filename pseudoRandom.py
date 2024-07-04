import random

x = random.randint(1,10)
y = random.random()
mylist = ['john','james','kilonzo']
z = random.choice(mylist)
cards = [1,2,3,4,5,6,7,8,9,"A","B","C","D"]

random.shuffle(cards)

print(cards)