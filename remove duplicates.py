def duplicates():
    a=[1,2,3,3,3,4,5]
    i=0
    l=[]
    while(i<len(a)):
        if a[i] not in l :
            l.append(a[i])
        i+=1
    print(l)
duplicates()