# Condition Expressions 
if(1==2):
    print("Universe stopped")
elif(1<2):
    print("Universe works")
elif(1>2):
    print("Universe stopped")
else:
    print("Nothing works")

try:
    age = int(input("Enter you age: "))
    if(age>=18):
        print("You can vote!")
    elif(age>=0):
        print("You can't vote")
    else:
        print("You are an inhuman")
except:
    print("Enter a number, not anything else")

a=int(input("Enter any number: "))
if(a<7):
    print("Less than 7")
elif(a<17):
    print("Less than 17")
elif(a<37):
    print("Less than 37")
elif(a<57):
    print("Less than 57")
elif(a<77):
    print("Less than 77")
elif(a<97):
    print("Less than 97")
else:
    print("Less than infinty")

# Relational and Logical Operators
if(a>=10):
    print("Greater or Equal to 10")
elif(not a>=10):
    print("Lesser or Equal to 10")

if(a>100 or a<0):
    print("Not in 0 to 100")


# Chapter 6 – Practice Set

# Write a program to find the greatest of four numbers entered by the user.
# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# num3 = int(input("Enter number 3: "))
# num4 = int(input("Enter number 4: "))

# if(num1>num4):
#     f1 = num1
# else:
#     f1 = num4
# if(num2>num3):
#     f2 = num2
# else:
#     f2 = num3
# if(f1>f2):
#     print(str(f1) + " is greatest")
# else:
#     print(str(f2) + " is greatest")

# Write a program to find out whether a student is pass or fail if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
# s1=int(input("Enter 1st subject marks: "))
# s2=int(input("Enter 2st subject marks: "))
# s3=int(input("Enter 3st subject marks: "))
# if(s1>33 and s2>33 and s3>33):
#     if((s1+s2+s3)/3>40):
#         print("You have Passed!")
#     else:
#         print("You have failed")
# else:
#         print("You have failed")

# A spam comment is defined as a text containing the following keywords:
# “make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.
# c=input("Enter a comment: ")
# c=c.lower()
# if("make a lot of money" in c or "buy now" in c or "subscribe this" in c or "click this" in c):
#     print("spam comment")
# else:
#     print("not a spam comment")

# Write a program to find whether a given username contains less than 10 characters or not.
c=input("Enter an username: ")
if(c.__len__()<10):
    print("It is less than 10 characters")
else:
    print("It is 10, or more than 10 characters")

# Write a program that finds out whether a given name is present in a list or not.
n=input("Enter a number: ")


# Write a program to calculate the grade of a student from his marks from the following scheme:
# 90+   A+
# 80-90	A
# 70-80	B
# 60-70	C
# 50-60	D
# <50	F


# Write a program to find out whether a given post is talking about “Harry” or not.