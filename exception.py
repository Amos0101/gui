
try:
    numerator = int(input("Enter a number to divide: "))
    denoinator = int(input("Enter a number to be divided: "))
    result = numerator/denoinator
except ZeroDivisionError:
    print("You can't divide by zero !!")
except ValueError:
    print("Enter an intenger")
except Exception:
    print("Something went wrong!!")
else:
    print(result)