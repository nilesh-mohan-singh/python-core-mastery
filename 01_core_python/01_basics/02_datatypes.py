# ***********Data Types************
# Integers 
# Strings
# Float
# Boolean
# None



# age = 23
# old = True
# a = None
# print(type(old))
# print(type(a))


# Keywords
# Keywords are reserved words in python
# Python is case-sensitive language



# Print Sum
# """
# a = 2
# b = 5
# sum = a+b
# print(sum)
# """


# Arithmetic Operators (+, -, *, /, %, **)
# Relational/Comparison Operators ( ==, !=, >, <, >=, <= )
# Assignment Operators ( =, +=, -=, *=, /=, %=, **=)
# Logical Operators (not, and, or)


# Type Conversion
# Type Casting


# Type Conversion
# a = 1
# b = 2.0
# sum = a + b
# print(sum)


# Type Casting
# a = 1
# b = "2"
# c = int(b)
# sum = a + c
# print(sum)

# Input in Python\
# Input() statement is used to accept values (using Keyboard) from user

# input()  # result for input() is always a str
# int(input()) # int
# float(input()) #float

# name = input("enter name:")
# age = int(input("enter age:"))
# marks = float(input("enter marks:"))

# print("welcome", name)
# print("age =", age)
# print("marks =", marks)



"""
Let's Practice
===============

1. Write a Program to input 2 numbers & print their sum

2. Write a Proggram to input sidde of a square & print its area.

3. WAP to input 2 floating pint numbers & print their avverage.

4. WAP to innput 2 int numbers, a and b. Print True if a greater than or equal to b. 
If not print False.
"""


# Solution 1
x = 2
y = 3
sum = x + y
print(sum)

# Solution 2
side = 4
area = side * side
print(area)

# Solution 3
a = float(2)
b = 3.2
avg = (a+b)/2
print(avg)

# Solution 4
a = int(4)
b = int(3)
if(a>b):
    print("True")
elif(a==b):
    print("True")
else:
    print("False")