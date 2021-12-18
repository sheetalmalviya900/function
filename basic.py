# # arguments
# def my_function(fname):
#       print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# # number arguments
# def my_function(fname, lname):
#       print(fname + " " + lname)

# my_function("Emil", "Refsnes")

# def my_function(fname, lname):
#       print(fname + " " + lname)
# my_function("Emil")

# def my_function(*kids):
#       print("The youngest child is " + kids[1])

# my_function("Emil", "Tobias", "Linus")

# num=1
# def fun():
#       num=3
#       print(num)
# fun()
# print(num)


#*args exapmle 
# if a number of arguments is unkown then we add *(args)
# def my_function(*kids):
#     print("the youngest child is ="+kids[2])
# my_function("emil","tobias","linus")



# # keyword arguments
# def my_function(c,b,a):
#     print("the youngest child is ="+a)
#     return
# my_function(a="emil",b="tobias",c="linus")

# # arbitary keyword
# # if a number of key argument is unkown then we add **(kwargs)
# def my_function(**kids):
#     print("the youngest child is ="+kids["lname"])
# my_function(fname="emil",lname="tobias",kname="linus")

# lambda function
# a lamba functioncan take a number of argument ,butonly have one arguments
x=lambda a:a+10
print(x(5))

# y=lambda a,b:a-b
# print(y(7,4))