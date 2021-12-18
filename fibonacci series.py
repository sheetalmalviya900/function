# def fib(n):  
#     """Print a Fibonacci series up to n."""
#     a,b=0,1
#     while a <= n:
#         print(a, end=',')
#         a, b = b, a+b
#     print()
# # Now call the function we just defined:
# fib(2000)


# i=0
# def greet():
#     global i
#     i+=1
#     print("hello",i)
#     greet()
# greet()

# def pattern(number):
#     if number == 1:
#         return 1
#     else:
# print(pattern(number-1) + 3)

def twopowers(number):
    if number==1:
        return 1
        return 2 * twopowers(number-1)

index=1
while(index<10):
    print(twopowers(index))
index+=1