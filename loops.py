# Loops

i = 10
while (i > 1):
    i = i - 1
    print(i)

a = ["CodeWithHarry", "Tech Gun", "Tech Burner"]
a.append("Singh in USA")
a.append("Zack King")
a.append("The Sarcastic Techynologion")
# print(a)

i = 0
while (i < a.__len__()):
    print(a[i])
    i = i + 1
print("\n")

for item in a:
    print(item)

for i in range(19):
    print(i)

for i in range(65, 75):
    if (chr(i) == 'E'):
        pass
    if (chr(i) == 'D'):
        continue
    if (chr(i) == 'G'):
        break
    print(chr(i))

# Chapter 7 – Practice Set
# Write a program to print the multiplication table of a given number using for loop.
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

# Attempt the above problem using a while loop.
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{n} x {i} = {n*i}")
    i = i + 1

# Write a program to greet all the person names stored in a list l1 and which starts with S.
l1 = ["Harry", "Sohan", "Sachin", "Rahul"]
for i in l1:
    if i.startswith('S'):
        print(i)

# Write a program to find whether a given number is prime or not.
n = int(input("Enter a number: "))
pr = True
for i in range(2, n):
    if (n % i == 0):
        pr = False
        break

if pr:
    print("It is a prime")
else:
    print("Not a prime")

# Write a program to find the sum of first n natural numbers using a while loop.
i = 1
sum = 0
n = int(input("Sum of numbers till: "))
while (i <= n):
    sum = sum + i
    i = i + 1
print("Sum is " + str(sum))

# Write a program to calculate the factorial of a given number using for loop.
i = 1
sum = 1
n = int(input("Factorial of: "))
while (i <= n):
    sum = sum * i
    i = i + 1
print("Factorial is " + str(sum))

# Write a program to print the following star pattern.
#     *
#    ***
#   ***** for n=3
n = int(input("Enter a number: "))
for i in range(n):
    print(" " * (n - i - 1), end="")
    print("*" * (2 * i + 1), end="")
    print(" " * (n - i - 1))

# Write a program to print the following star pattern:
#  *
#  **
#  *** for n = 3
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print("*" * i)

# Write a program to print the following star pattern:
# * * *
# *   *             #For n=3
# * * *
n = int(input("Enter a number: "))
print("* " * n)
print((("*" * 1) + ("  " * (n - 2)) + (" *" * 1) + "\n") * (n - 2), end="")
print("* " * n)

# Write a program to print the multiplication table of n using for loop in reversed order.
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {11-i} = {n*(11-i)}")