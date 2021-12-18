def string():
    name=str(input("Enter the name :"))
    name1=str(input("enter the name :"))
    if(len(name)>len(name1)):
        print(name)
    if(len(name1)>len(name)):
        print(name1)
    if(len(name)==len(name1)):
        print(name)
        print(name1)
string()