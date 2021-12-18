def prime():
    limit=int(input("enter the number"))
    i=1
    while(i<=limit):
        count=0
        j=1
        while(j<=i):
            if(i%j==0):
                count+=1
            j=j+1
        if(count==2):
            print(i,"is the prime number")
        i+=1
prime()
