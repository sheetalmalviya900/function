def string():
    list=["abc",'xyz','aba','1221',"cac"]
    i=0
    result=0
    while(i<len(list)):
        if(list[i][0]==list[i][-1]):
            result+=1
        i+=1
    print("result=",result)
string()