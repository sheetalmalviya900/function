def limit():
    limit=int(input("Enter the number"))
    sum=0
    sum1=0
    i=0
    while(i<=limit):
        if(i%5==0):
            sum+=i
        if(i%3==0):
            sum1=sum1+i
        i+=1
    print(sum+sum1)
limit()