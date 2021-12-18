def mass():
    bmi=int(input("enter the bmi"))
    if(bmi<=18.5):
        print("underweight")
    elif (bmi<=25.0):
        print("normal")
    elif(bmi<=30.0):
        print("overweight")
    elif(bmi>30):
        print("obese")
mass()