# #single:- 1 parent 1 child
# class Cars:
#     def car(self):
#           print("thus is  a car")
# class Honda(Cars):
#         def honda(self):
#               print("thus is hondda car")
# h1=Honda()
# h1.honda()
# h1.car()

#MULTI LEVEL{ 1 P 1CHILD THAT CHILD IS PARENT FOR OTHER CHILD}

# class Grandparent:
#       def gp(self):
#             print(" this is a grand parents class")

# class Parents(Grandparent):
#       def par(Self):
#             print("this is parent class")

# class Child(Parents):
#       def chids(Self):
#             print("this is a child class")

# c1=Child()
# c1.gp()
# c1.par()
# c1.chids()


#HIERARCHICAL INNHERITENCE (1 PARENT MULTI CHILD)
# class Company:
#       def company(self):
#             print("thus is a comaney")
# class Employee(Company):
#       def emp(self):
#             print("this is emp class")
# class Hr(Company):
#       def hr(self):
#             print("this is a hr clss")
# h1=Company()
# h1.company()
# e1=Employee()
# e1.emp()
# g1=Hr()
# g1.hr()


#MULTIPLE INHERITANCE { MULTI PARENTS AND 1 CHILD}
# class father :
#     def par(self):
#         print("this is aparent class")
#     def mot(self):
#         print(" this is moto class")
# class Mother:
#     def cook(self):
#         print("she cook")
#     def wash(self):
#         print("she wash")

# class Child(father,Mother):
#     def child(self):
#         print(" this is a child")
# c1=Child()
# c1.par()
# c1.mot()
# c1.cook()
# c1.wash()
# c1.child()

#hybrid inheritance { combination of 2 or more in heritance}
class A:
    def a(self):
        print("this is a")
class B(A):# here b is 1 parent thaat is child for c and d
    def b(self):
        print("this is b")
class C(B):
    def c(self):
        print(" this is a c clsss")
class D(C,B):
    def d(self):

        print("thus us d class")
d=D()
d.a()
d.b()
d.c()
d.d()





