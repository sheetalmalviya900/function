def primeorNot(num):
    a=1
    count=0
    while(a<=num):
        if(num%a==0):
            count+=1
        a=a+1
    if(count==2):
        print("prime number")
    else:
        print("composite number")
primeorNot(7)