#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

if last_digit > 5:
    str_format = 'Last digit of {0} is {1} and is greater than 5'
elif last_digit < 6 and last_digit != 0:
    str_format = 'Last digit of {0} is {1} and is less than 6 and not 0'
else:
    str_format = 'Last digit of {0} is {1} and is 0'

result = str_format.format(number, last_digit)
print(result)
