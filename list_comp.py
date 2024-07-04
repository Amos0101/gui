# list comprehensions = a way to create a new list with less syntax
#                       can mimic certain lamda functions, easier to read
#                       list = [expression for item in iterable]

squares = [] # create an empty list
for i in range(1,11):  #create a for loop
    squares.append(i * i) # define what each loop iterartion should do
print(squares)

# using list comprehensions
squares = [i * i for i in range(1,11)]
print(squares)