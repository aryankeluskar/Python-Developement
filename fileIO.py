# Modes of opening a file
# r – open for reading
# w – open for writing
# a – open for appending
# + -> open for updating
# ‘rb’ will open for read in binary mode
# ‘rt’ will open for read in text mode

f = open("sample.txt")
data=f.read()
print(data)

f.close()

f = open("sample.txt", "a")
f.write("\nI am writing")

f.close()

with open("sample.txt", "r") as f:
    print(f.read())

# Chapter 9 – Practice Set

# Write a program to read the text from a given file, "sample.txt” and find out whether it contains the word ‘twinkle’.
f=open("practice.txt", "r")
if "twinkle" in f.read().lower():
    print("twinkle is there")
else:
    print("twinkle is not there")

# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file “Hiscore.txt” which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever game() breaks the Hi-Score.
import random
def game():
    return random.randint(1,100)

f=open("practice.txt", "r")
# if " " == f.read() :
#     fw=open("practice.txt", "w")
#     fw.write(str(0))
#     fw.close()
play=game()
print("Read: "+f.read())
if(int(f.read())<play):
    print(f.read())
    print("High Score broken")
    fw=open("practice.txt", "w")
    fw.write(str(play))
    fw.close()
f.close()