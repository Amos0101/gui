#alive = True
#print(alive)

#print(alive := True)
"""
#without using a walrus operator
foods = list()

while True:
    food = input("Which food do you like?: ")
    if food == "quit":
        break
    foods.append(food)
print(foods, end=" ")
"""

foods = list()
while food := input("Which food do you like?: ") !="quit":
    foods.append(food)
    break
