def positivenegative():
    list=[1,-7,8,-6,-9,-4,5,9,]
    positive=0
    negative=0
    i=0
    while(i<len(list)):
        if(list[i]<0):
            negative+=1
        else:
            positive+=1
        i+=1
    print("negative number in these list",negative)
    print("positive number in these list",positive)
positivenegative()