def fizz_buzz():
    nm=int(input("enter the number"))
    if (nm%3==0 and nm%5==0):
        print("FizzBuzz")
    elif(nm%3==0):
        print("Fizz")
    elif(nm%5==0):
        print("Buzz")
    else:
        print(nm)
fizz_buzz()