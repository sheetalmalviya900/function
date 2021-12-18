# def my_function(a):
#     list=['a','1','2','5','b','q']
#     print(list[-a])
# my_function(1)
# my_function(3)
# my_function(4)

def my_function():
    list=['a','1','2','5','b','q']
    num=int(input("enter the number:-"))
    i=1
    while(i<=num):
        print(list[-i])
        i+=1
my_function()
        