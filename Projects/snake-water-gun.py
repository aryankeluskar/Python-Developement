import random
print("Enter (1) for Rock, (2) for Paper, (3) for Scissor")

a=input("Player turn: ")
a=int(a)
if(a<1):
    a=1
if(a>3):
    a=3

c= random.randint(1,3)

if(a==c):
    print("Tie!"+"; Computer chose:"+str(c) )
elif(a==1 and c==3):
    print("You Won"+"; Computer chose:"+str(c) )
elif(a==2 and c==3):
    print("You Lost"+"; Computer chose:"+str(c) )
elif(a==1 and c==2):
    print("You Won"+"; Computer chose:"+str(c) )
elif(a==3 and c==2):
    print("You Won"+"; Computer chose:"+str(c) )
elif(a==2 and c==1):
    print("You Lost"+"; Computer chose:"+str(c) )
elif(a==3 and c==1):
    print("You Lost"+"; Computer chose:"+str(c) )