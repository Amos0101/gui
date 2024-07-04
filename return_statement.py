"""def multiply(num1,num2):
    result = num1*num2
    return result

print(multiply(3,5))"""

#multiple args
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1, 2, 3,4,5,6))


