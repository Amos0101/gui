from Car import car

car_1 = car("chenvy","challote",2020,"white")
car_2 = car("cord","mastug",2022,"brown")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.stop()
car_1.drive()

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_2.stop()
car_2.drive()