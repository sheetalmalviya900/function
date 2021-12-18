def reverse():
    name=str(input("enter the name :"))
    i=1
    while(i<=len(name)):
        print(name[-i],end="")
        i+=1
reverse()