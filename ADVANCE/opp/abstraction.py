# # ABSTRACTION:-hideing complex implimentation and showing essential

# from abc import ABC,abstractmethod
# class Vehical(ABC):
#     @abstractmethod
   
#     def start(self):#not show imp 
#         pass
# class BMW(Vehical) :
#     def start(self):
#         print("car us started")
# c1=BMW()
# c1.start()

"""
super:- it is usesd to access a  meathod which has a same method namea and which
is indide a patrent class 
"""
# from abc import ABC,abstractmethod
# class Shape:
#     @abstractmethod
#     def area(self):
#         print("calcuataing area")
# class  Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         # super().area() # without this chid overides parent 
#         result=3.14*self.radius*self.radius
#         print(f"area of circle is {result}")
# cl=Circle(7)
# cl.area() 

# class Animal:
#     def dog(self):
#         print("dog bark")
# class Pets(Animal):
#     def dog(self):
#         print("dog eats")
#         super().dog()
# cl=Pets()
# cl.dog()

from abc import ABC,abstractmethod
class Vehical(ABC):
    @abstractmethod
    def start():
        pass
class Car(Vehical):
    def start(self):
        print("car started")
        
        
c1=Car()
c1.start()

class Animals:
    def dog(self):
        print("dog eat")
class Pet(Animals):
    def dog(self):
        print("dog bark")
        super().dog()
m1=Pet()
m1.dog()

    






