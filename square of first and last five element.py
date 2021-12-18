def element():
    limit=int(input("enter the limit : "))
    a=[]
    b=[]
    i=1
    while(i<=5):
        k=i**2
        a.append(k)
        i+=1
    s=limit-4
    while(s<=limit):
        k=s**2
        b.append(k)
        s+=1
    print(a,b)
element()