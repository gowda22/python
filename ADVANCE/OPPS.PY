# class Student:
#     def __init__(self,name,cls_name):
    
#         self.name=name
#         self.cls_name=cls_name
#         self.school="hms"
#     def show(self):
#         print(f""" {self.name} is from {self.cls_name} class""")

# a=Student("gowda","10th" )
# a.show()


class Car:
    def __init__(self,brand,color,seats):
        self.brand=brand
        self.color=color
        self.seats=seats
        self.engine="pertol"

    def start(self):
        print("car is started")
    def stop(self):
        print("car is stopped")

    def details(self):
        print(f""" the car brand is {self.brand}and colour is{self.color}it 
        has {self.seats}seats and it is {self.engine} engine""")

a=Car("bmw","black","7")
a.start()
a.stop()
a.details()



       
