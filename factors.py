def factor():
    i=1
    sum=0
    while(i<=1000):
        j=1
        sum=0
        while(j<i):
            if(i%j==0):
                sum+=j
            j+=1
        if(sum==i):
            print(i,"is perfect number")
        i+=1
factor()    

