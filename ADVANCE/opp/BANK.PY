# class Bank:
#     def __init__(self,name,acc_no,ball):
    
#         self.name=name
#         self.acc_no=acc_no
#         self.ball=ball
#     def deposit(self,deposit_amount):
#         if deposit_amount>0:
#             self.ball+=deposit_amount
#             print(f"{deposit_amount} deposite success AND ur cuttent sal is {self.ball}")
#         else:
#             print("kindly enter valid no")
#     def withdraw(self,withdraw_amount):
#         if withdraw_amount>self.ball:
#             print("insufficient fund..")
#         else:
#             self.ball-=withdraw_amount
#             print(f"{withdraw_amount} withdraw successs")
#     def show_balence(self):
#         print("you r current balance",self.ball)
# B1=Bank("gowda",75757573,50000)
# B1.deposit(10000)
# B1.withdraw(30000)
# B1.show_balence()


class Bank:
    def __init__(self,name,accno,balence):
        self.name=name
        self.accno=accno
        self.balence=balence
        self.totalbal=0
        self.with_bal=0

    def deposit(self,dep_amt):
        if dep_amt<=0:
            print("kindly enter valid no")
        else:
            self.balence += dep_amt
            self.totalbal+=dep_amt
            print(f"""{dep_amt} amount deposit successfully
                   and ur current balence is {self.balence}""")

    def withdraw(self,withdraw_amt):
        if withdraw_amt>=self.balence:
            print("insufficient fund")
        else:
            self.balence-=withdraw_amt
            self.with_bal-=withdraw_amt            
            print(f"""{withdraw_amt}amount successfully withdraw
            and ur current balance is {self.balence}""")
    def details(self):
        print(f""" ur  name is {self.name} and ur accountno is {self.accno}
you  r deposited  is {self.totalbal}then u withdraw {self.with_bal}and ur current balence is {self.balence}""")
        
B1=Bank("gowda",6546747747,50000)
B1.deposit(5000)
B1.withdraw(10000)
B1.details()




