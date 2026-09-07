# #DECORATORS(FUN THAT MODIFY OTHER FUN WITHOUT CHANGE ORIGINAL CODE)
# # Authentication and authorization, input validation, access control. 

# #WITHOUT DECORATOR
# def greet():
#     print("hello")

# def my_decorator(func):
#     def wrapper():
#         print("before exe")
#         func()
#         print("after exe")

#     return wrapper
# greet1=my_decorator(greet)
# greet1()

#WITH DECORATOR
# def my_decorator(func):
#     def wrapper():
#         print("before exe")
#         func()
#         print("after exe")

#     return wrapper
# @my_decorator 
# def greet():
#     print("hello")
# greet()

# #DECORATORS WITH {ARGUMENTS}{divion}
# def smart_divison(func):
#     def wrapper(a,b):
#         if b==0:
#             return " can not divide"
#         return wrapper
# @smart_divison
# def divide(a,b):
#     return(a/b)
# print(divide(10,2))
# print(divide(10,0))

#GENERATOR{PRODUCE VALUES 1 AT A TIME USING YIELD}
# def numbers():
#     return[1,2,3,4]# 1,2,3,4 ALL VAL IN 1 SHOT
# def num():
#     yield 1
    
#     yield 2
#     yield 3
#     yield 4
#     yield 5
# s=num()
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))

#GENATAROR WITH LOOP
def even(n):
    for i in range(2,n+1,2):
        yield i
for j in even(10):
    print(j)

    

