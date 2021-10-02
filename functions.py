# Function

marks=[78,97,89,78,97,82]
def percent(marks):
    sum=0
    for i in marks:
        sum+=i
    return round((sum/marks.__len__()), 2)
print(percent(marks))

def greet(name="Stranger"):
    print(f"Good Day, {name}")
greet("Aryan")

def fact_recur(n):
    n=int(n)
    if(n==0):
        return 1
    return n*fact_recur(n-1)
print(fact_recur(9))


# Chapter 8 – Practice Set

# Write a program using the function to find the greatest of three numbers.
n2=2346894
n1=4286093
n3=4698435
def greatest(a,b,c):
    if(a>b):
        if(a>c):
            return a
        return c
    if(b>c):
        if(b>a):
            return b
        return a
    return 0
print(greatest(n1,n2,n3))

# Write a python program using the function to convert Celsius to Fahrenheit.
def CToF(C):
    C = int(C)
    return round((C * (9/5)) + 32, 1)
print(CToF(42))

# How do you prevent a python print() function to print a new line at the end?
print("This wont start on a new line", end="")
print("Did it?")

# Write a recursive function to calculate the sum of first n natural numbers.
def sum_recur(n):
    n=int(n)
    if(n==1):
        return 1
    return n+sum_recur(n-1)
print(sum_recur(12))

# Write a python function to print the first n lines of the following pattern.
# ***
# **       #For n = 3
# *
def pattern(n):
    for i in range(n):
        print("*"*(n-i))
pattern(6)

# Write a python function that converts inches to cms.
def InToCm(i):
    i=int(i)
    return round(i*2.54, 2)
print(InToCm(45))

# Write a python function to remove a given word from a string and strip it at the same time.
s = "Hi, I am   Aryan  "
def rep_and_strip(str, word):
    str = str.replace(word, "").strip()
    word=word.strip()
    print(str+'\n'+ word)
rep_and_strip(s, "Aryan")

# Write a python function to print the multiplication table of a given number.
def table(n):
    n=int(n)
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
table(23)

