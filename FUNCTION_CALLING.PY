# # FUNCTION CALLING ANOTHER FUN
# def square(n):
#     print(n*n)
# def show(x):
#     square(x)
# show(4)

# factorial
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n* factorial(n-1)
# print(factorial(5))

# PRINT ND RETURN 
# def sqare(n):
#     print(n*n)
# sqare(7) #BY  PRINT ST

# def square(n):
#     return(n*n)
# x=square(5) #it print nd store val
# print(x)
# y=x+22
# print(y)
# z=y*2# we can not do this print it show error
# print(z)

# SCOPES{which variable which position}

# x=20
# def sam(x):
#     print(x)
# sam(10)
# x+=10
# print(x)

#LOCAAL variable{inside only}
# def function():
#     x=30
#     print("inside function x = ",x)
# function()
# print(x)#error not acc by outside

#global variale{var def out can acces in and outside }
# y=20
# def fun():
#     y+=70 # but not modify??
#     print(y)#20
# fun()
# y+=10 #30
# print(y)

#TOD DO USE GLOBAL KEYWORD
# y=20
# def fun():
#     global y
#     y+=10 # inn
#     print(y)#30
# fun()
# y+=10 #40 bcz inside it incc byb 10=30 so 40
# print(y)

# def outer():
#     a=10
#     def inner():
#         # a+=10 error 
#         print(a) #innr op
#     inner()
#     print(a)#outer op
# outer()

#NON LACAL KEYWORD [USE IN SUB FUNS]
def  outer():
    a=10
    def inner():
        nonlocal a
        a+=10
        print(a)#20
    inner()
    print(a)#20 bcz indei inner it modified
outer()
    


