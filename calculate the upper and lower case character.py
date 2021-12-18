def string():
    text=str(input("enter the number :"))
    upper=0
    lower=0
    i=0
    while(i<len(text)):
        if(text[i])>="A" and (text[i])<="Z":
            upper+=1
        if(text[i])>="a" and (text[i])<="z":
            lower+=1
        i+=1
    print("upper =",upper)
    print("lower =",lower)     
string()
