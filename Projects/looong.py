f=open("msg.txt", "w")
i=1
while(i<1000):
    i=i+1
    f.write("\n")
    if(i%100==0):
        f.write("almost there, keep scrolling down")