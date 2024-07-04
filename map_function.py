#map() = applies a function to each item in the iterable(lists,tuples)
# map(function,iterable)

store = [("shirt",20.00),
         ("trouser",43.00),
         ("pants",12.00),
         ("sorks",6.00)]

to_euros = lambda data:(data[0],data[1]*0.82)
to_dollars = lambda data:(data[0],data[1]*140)

store_dollars = list(map(to_dollars,store))

for i in store_dollars:
    print(i)
