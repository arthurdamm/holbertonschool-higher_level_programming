#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("The last digit of {:d} is {:d} and is ".format(number, number % 10), end="")
if number % 10 > 5:
    print("greater than 5")
elif number % 10 == 0:
    print("0")
else:
    print("and is less than 6 and not 0")
