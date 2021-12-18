def square():
    num=str(input("enter the number:"))
    i=0
    while(i<len(num)):
        print(int(num[i])**2,end="")
        i+=1
square()