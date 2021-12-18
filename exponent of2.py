def exponent():
    n=int(input("enter the number :"))
    l=[]
    i=0
    while(i<=n):
        k=2**i
        l.append(k)
        print(l)
        i+=1
exponent()