# Lists (Mutable Array)
a = ["CodeWithHarry", "Tech Gun", "Tech Burner"]
print(a, a[0])

# Append, Insert, Pop and Remove
a.append("Singh in USA")
a.append("Zack King")
a.append("The Sarcastic Techynologion") # Adds at end
a.insert(1,"MrWhoseTheBoss")            # Adds at an index
print(a)
a.pop(3)                    # Removes from Index
a.remove("Singh in USA")    # Removes first occurence
print(a)
print(a.__contains__("MrWhoseTheBoss"), a.__len__(), a.index("Tech Gun"))

# Slicing
print(a[3:6])
print(a[-2:])

# Sorting, Reversing
a=[6,3,8,2,5,7,3,1,6,8,9]
a.sort()
a.reverse()
print(a)


# Tuples (Immutable Array)
t=("CodeWithHarry", "Tech Gun", "Tech Burner")
# t[0]="Thapa Technical" => TypeError: 'tuple' object does not support item assignment


# Chapter 4 – Practice Set

# Write a program to store three fruits in a list entered by the user.
m=[]
m.append(input("Enter a fruit: "))
m.append(input("Enter a fruit: "))
m.append(input("Enter a fruit: "))
print(m)

# Write a program to accept the marks of 6 students and display them in a sorted manner.
m.clear()
m.append(int(input("Enter marks of Student 1: ")))
m.append(int(input("Enter marks of Student 2: ")))
m.append(int(input("Enter marks of Student 3: ")))
m.append(int(input("Enter marks of Student 4: ")))
m.append(int(input("Enter marks of Student 5: ")))
m.sort()
print(m)

# Write a program to sum the above marks list

print("Sum of Marks: ", sum(m))

# Write a program to count the number of zeros in the following tuple:
a = (7, 0, 8, 0, 0, 9)
print("Count of Zeroes: ",a.count(0))