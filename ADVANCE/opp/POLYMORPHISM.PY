# """
# POLYMORPHISM:- SAME METHOD NAME PERFROMS DIFFRENTLY
# 1 NAME MANY FROMS
# """
# # FUNCTION POLY: same function name works diffrently
# print(len("python"))
# print(len([4,34,5,4]))

# #operator poly:- same opetrator behaves diffrently
# print(10+20)
# print("hello" + "gowda")

#method overloading:- having multiple methods with same methis name but diff
# parameter{not supported we archive by default args and variable lenth arg {*args}}

# class Calculator:
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c=0):
#         print(a+b+c)
# c1=Calculator()
# c1.add(10,20,20)
# c1.add(10,20) # erroe

# class Addition:
#     def add(self,*args):
#         print(sum(args))
# a1=Addition()
# a1.add(10,303,45,777,8,8,9,9,9,)


"""
METHOD OVERRIDING:-whn child cls provides its own implimentation of a method
which is alredy definmed in parent class
use super ()

"""

class Parent:
    def fun(self):
        print(" this is a parent function")
class Child(Parent):
    def fun(self):
        super().fun()
        print(" this is a child class")
c1=Child()
c1.fun()
       