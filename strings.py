# Strings
s= "Aryan"
s='Hi'
s='''I want holidays 🥺'''
print(s, type(s))
s='Aryan\'s Websites' #Escape Sequence
b=", "

print(f"This is easy concatenation{s}{b}{56}")

# String Concat, Indexing, Slicing
s1=" and his YouTube Channels Rock!"
print(s+s1)
print(s[1], s1[5], s[-3])       # Negative indices start from -1 from end
print(s[:5], s1[1:8], s1[-5:])  # :5 is same as 0:5. 6: is same as 6:end
print(s[0:10:3]) #every 3rd character is printed in the given range

# String Functions
s="         hi, this is strip               "
print(s.strip(" "))
s="aryan is aryan, not aaryan, only aryan"
print("Length:",len(s),b, s.endswith("yan"),b, s.count('a'),b, s.find('not'))
print(s.replace('aryan','harry'),b, s.upper())


# Chapter 3 – Practice Set

# Write a Python program to display a user-entered name followed by Good Afternoon using input() function.
s=input('\nEnter your name: ')
print("Good Afternoon, "+s)

# Write a program to fill in a letter template given below with name and date.
from datetime import date
print("\nLetter:\n"+'''Dear {}
You are selected!!
Date: {}'''.format(s,date.today()))

# Write a program to detect double spaces in a string.
s=input('\nEnter anything: ')
print('Number of double spaces:',s.count("  "))

# Replace the double spaces from problem 3 with single spaces.
print(s.replace("  ","   "))