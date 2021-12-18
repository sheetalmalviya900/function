def oddeven():
    i=1
    while i<10:
        num=int(input("enter the number:"))
        if(num%2==0):
            print(num*100)
        else:
            print(-num)
        i+=1    
oddeven()