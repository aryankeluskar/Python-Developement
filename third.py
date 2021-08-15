# Strings
s= "Aryan"
s='Hi'
s='''I want holidays 🥺'''
print(s, type(s))
s='Aryan\'s Websites' #Escape Sequence

# String Concat, Indexing, Slicing
s1=" and his YouTube Channels Rock!"
print(s+s1)
print(s[1], s1[5], s[-3])       # Negative indices start from -1 from end
print(s[:5], s1[1:8], s1[-5:])  # :5 is same as 0:5. 6: is same as 6:end
print(s[0:10:3]) #every 3rd character is printed in the given range

# String Functions