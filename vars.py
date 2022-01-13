# Variable, Datatypes
n = "Aryan"
a = 15
great_people = ["Tech Burner", "Tech Gun", "CodeWithHarry"]
b = ", "
boo = True
no = None
f = 4.21
print(n, b, a, b, f, b, great_people, boo)
print(type(n), type(f), type(b), type(great_people), type(a))

# Operators
print(10 / 7, 32 - 34, 756 + 344, 2 * 86, 85 % 6)
print(10 == 10, 43 == 23, 5 != 4, 5 < 0, 53 > 42)
print(True and False, True or False, not True)

# Conversion
print(str(a) + n, b, float(a))
n = "273"
print(a + int(n) + int(boo))

#Input
n = input('Enter your name: ')
print(
    n,
    "is running this program, because he knows how to access this, his type is",
    type(n))

# Chapter 2 – Practice Set

# Write a Python program to add two numbers.
c = int(input('Enter a number: '))
Z = int(input('Enter a number: '))
print("Sum:", c + Z)

# Write a Python program to find the remainder when a number is divided by Z(Integer).
print("Remainder", c % Z)

# Check the type of the variable assigned using the input() function.
print(type(input("Enter anything: ")))

# Use a comparison operator to find out whether a given variable a is greater than b or not. (Take a=34 and b=80)
print("Is c>Z: ", (c > Z))

# Write a Python program to find the average of two numbers entered by the user.
print('Average of c and Z', (c + Z) / 2)

# Write a Python program to calculate the square of a number entered by the user.
print("Square of c is ", c * c)
