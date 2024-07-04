#filter() = creates a collection of elements from an iterable to which a funcyion returns true
# filter(funtion,iterable)

friends = [("kaimosi",23),
           ("kitunusi",21),
           ("mulongo",17),
           ("mkuru",16),
           ("mwenza",28)]

age =lambda data:data[1] >= 18

alcoholics = list(filter(age,friends))

for i in alcoholics:
    print(i)


