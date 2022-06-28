#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    print(f"the last digit of {number} is {number % 10}")
else:
    print(f"the last digit of {number} is {((number * -1) % 10)}")
