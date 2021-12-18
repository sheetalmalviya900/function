def showNumbers():
    limit=int(input("enter the number"))
    i=0
    while(i<=limit):
        if(i%2==0):
            print(i,"is even")
        else:
            print(i,"is odd")
        i+=1
showNumbers()