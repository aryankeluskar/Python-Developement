# Dictionary
d = {
    "Aryan": "a bored student",
    "Vision 40": "piece of s"
}
print(type(d), d, d['Vision 40'], d["Aryan"])
d["Vision 40"]="college life spoiler" 
print(d["Vision 40"])
d["holidays"]="404 not found"
d["classes"]="torture"
d["understanding"]=0
print("Length",d.__len__())

# Methods
print(d.keys(), d.values())
print(list(d.items())[1])
d2={
    "Aryan": "No wish to live",
    "exam prep":0
}
d.update(d2) # merges d2 into d
print(d)

print("Get:", d.get("aryan")) # returns None if not present 
try:
    print("Normal:", d["aryan"])  # throws an error is not present
except:
    print()

# Sets
s={6,5,7,3,6,8,3,5,6,7,8,5,4,2,2,4,5,6,7}
# No repetetition allowed!
print(type(s), s)

# Set Methods
s.add(12)
s.add(1)
s.add(1) # 1 will be added only once
try:
    s.add([1, 3, 4])  # will return an error List inside Set
    s.add({1:2, 3:4}) # will return an error Dictionary inside Set
except:
    a=0
s.add((11,31,41)) # will accept Tuple inside Set
print(s)

s.remove(1)
s.remove(7)
print(s)

print("Length", s.__len__())

print(s.pop()) # Removes arbitary element
print(s)

print(s.union({2,31,5,3,7}))
print(s.intersection({2,31,5,3,7}))
s.clear()
d={} # Empty Dictionary
s=set() # Empty Set


# Chapter 5 – Practice Set

# Write a program to create a dictionary of Hindi words with values as their English translation. Provide the user with an option to look it up!
eToH = {
    "Padhai": "Study",
    "Vastu": "Item",
    "Pathshala": "School"
}
print("Options are:",eToH.keys())
in_1=input("choose one of the above to translate: ") 
print(eToH.get(in_1))


# Write a program to input four numbers from the user and display all the unique numbers (once).
s=set()
i=1
while(i<=4):
    i=i+1
    s.add(input("Enter any number: "))
print(s)

# Can we have a set with 18(int) and “18”(str) as a value in it?
s={18, "18"}
print(s.__len__(), s)

# What will be the length of the following set S:
# S = set()
# S.add(20)
# S.add(20.0) # wont be considered
# S.add("20")
# What will be the length of S after the above operations?
# print(S.__len__(), S)
Answer="Length is 2, since 20.0 and 20 are regarded as same"

# S = {}, what is the type of S?
Answer = "Dictionary"


# Create an empty dictionary. Allow 4 friends to enter their favorite language as values and use keys as their names. Assume that the names are unique.
friends={}
i=1
while i<=4:
    name=input("Enter your name: ")
    friends[name]=input("Enter your favourite language: ")
    i=i+1
print("Friends are:", list(friends.keys()))
in_1=input("choose one of the above to get their fav language: ") 
print(friends.get(in_1))
# If the names of 2 friends are the same; what will happen to the program in Program 6?
Answer="The latest value will be in the Set, the previous value will be ignored"
# If the languages of two friends are the same; what will happen to the program in Program 6?
Answer="No change"

# Can you change the values inside a list which is contained in set S
# S = {8, 7, 12, “Harry”, [1, 2]}
Answer="Set is faulty, since it contains a List"