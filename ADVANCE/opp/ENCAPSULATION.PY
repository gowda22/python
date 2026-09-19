# #BUNDLING METHODA ND DATA IN  A CLASS AND IT CONTROLES ACCES DATA

# #access specifier
# """ 
# 1.public n=1000
# 2.private __bal=22
# 3.protecte _bal=3222
# """

# class Bankaccont:
#     def __init__(self,name,balance):
#         self.name=name# public
#         self.__bal=balance# private
#         # self.__balace=50000 we an acces this {print(b._Bank__balance)}
# b1=Bankaccont("gowda",10000)
# print(f" ur name is {b1.name}")
# print(b1.balance()) # error

# print(b1.balance) bcz its ptivate

#TO ACCES AND MODIFYB WE HAVE 
# GETTER= ACCESS AND SETTER TO MODIFY


# class Bankaccont:
#     def __init__(self,name,balance):
#         self.name=name# public
#         self.__bal=balance# private
#     #GETTER
#     def get_bal(self):
#         return self.__bal
#     def depsit(self,amount):
#         if amount>0:
#             self.__bal+=amount
#             print(f"{amount}deposit sucessfully and ur bal is{self.__bal}")
#         else:
#             print(" kindlyu enter crt amt")
# b1=Bankaccont("gowda",10000)
# b1.depsit(5000)


#ENCAPSULATION {PROTECTED USE INHERITANCE}
class Employee:
    def __init__(self,name,sal):
        self.name=name
        self._salry=sal
class Manager(Employee):
    def show_sal(self):
        print(self._salry)
c1=Manager("alain",100000)
c1.show_sal()




    

        

    









   