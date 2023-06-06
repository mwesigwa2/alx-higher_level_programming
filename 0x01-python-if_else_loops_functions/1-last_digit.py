#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def last(number):
    last_digit = abs(number) % 10
    return -last_digit if (number < 0) else last_digit


last_no = last(number)
if last_no > 5:
    print(f"Last digit of {number} is {last_no} and is greater than 5")
elif last_no == 0:
    print(f"Last digit of {number} is {last_no} and is 0")
else:
    print(f"Last digit of {number} is {last_no} and is less than 6 and not 0")
