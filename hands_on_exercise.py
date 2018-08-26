"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print('Value of pi is', pi, 'and its type is', type(3.14))


# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
print('i=', i)
if i < 50:
    print('i is less than 50')
else:
    print('i is greater than 50')


# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picked_fruit == 'orange':
    print('colour of the fruit is orange')
elif picked_fruit == 'strawberry':
    print('colour of the fruit is red')
else:
    print('colour of the fruit is yellow')


# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def mult(num1, num2):
    result = num1 * num2
    return result

# TODO: Now call the function a few times to calculate the following answers
a = mult(12, 96)
print("12 x 96 =", a)
b = mult(48, 17)
print("48 x 17 =", b)
c = mult(196523, 87323)
print("196523 x 87323 =", c)
