# # class Student:
# #     def __init__(self,name,cls_name):
    
# #         self.name=name
# #         self.cls_name=cls_name
# #         self.school="hms"
# #     def show(self):
# #         print(f""" {self.name} is from {self.cls_name} class""")

# # a=Student("gowda","10th" )
# # a.show()


# class Car:
#     def __init__(self,brand,color,seats):
#         self.brand=brand
#         self.color=color
#         self.seats=seats
#         self.engine="pertol"

#     def start(self):
#         print("car is started")
#     def stop(
#             self):
#         print("car is stopped")

#     def details(self):
#         print(f""" the car brand is {self.brand}and colour is{self.color}it 
#         has {self.seats}seats and it is {self.engine} engine""")

# a=Car("bmw","black","7")
# a.start()
# a.stop()
# a.details()
class Bank:
    def __init__(self,name,acc_no,ball):
    
        self.name=name
        self.acc_no=acc_no
        self.ball=ball
    def deposit(self,deposit_amount):
        if deposit_amount>0:
            self.ball+=deposit_amount
            print(f"{deposit_amount} deposite success")
        else:
            print("kindly enter valid no")
    def withdraw(self,withdraw_amount):
        if withdraw_amount>self.ball:
            print("insufficient fund..")
        else:
            self.ball-=withdraw_amount
            print(f"{withdraw_amount} withdraw successs")
    def show_balence(self):
        print("you r current balance",self.ball)
B1=Bank("gowda",75757573,50000)
B1.deposit(10000)
B1.withdraw(30000)
B1.show_balence()

             

   





