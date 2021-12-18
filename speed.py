def speed():
    speed=int(input("Enter the number"))
    if(speed<=70):
        print("ok")
    elif(speed>70):
        point=(speed-70)//5
        if(point<12):
            print("your point is",point)
        elif(point>=12):
            print("license suspend")
speed()   