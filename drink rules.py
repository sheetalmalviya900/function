def drink():
    age=int(input("enter the age "))
    if (age<=14):
        print(age,"drink toddy")
    elif(age<=18):
        print(age,"drink coke")
    elif(age<=21):
        print(age,"drink beer")
    else:
        print(age,"drink whisky")
drink()