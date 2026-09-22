# """ 
# manuallyb rize exception using rize keyword 

# """
# # def withdraw(amount):
# #     if amount>10000:
# #         raise ValueError ("withdraw limit excess")
# #     else:
# #         print(f"{amount} withdraw successfull")
# # try:
# #     withdraw(50000)
# # except ValueError as e:
# #     print("error",e)

# """
# user defind exception created by programmer whn a specific condition occurs
# uses Excepetion class and it the base classs inheritate by exception

# """
# # class InvalidageError(Exception):
# #     pass
# # def agecheck(age):
# #     if age<18:
# #         raise InvalidageError("this is in valid")
# #     else:
# #         print(f" ur age is {age}  eligible to vote")
# # try:
# #     agecheck(121)
# # except InvalidageError as e:
# #     print("Error:-",e)

# def age_chk(age):
#     if age<18:
#        raise ValueError ("invalid age")
#     else:
#         print("valid")



# try:
    
    
#     d=age_chk(12)
# except  ValueError as e :
#     print("error",e)
# else:
#     print(" no error")
# finally:
#     print("completed")





class Invalidage(Exception):
    pass
def fun(age):
    if age <18:
        raise Invalidage ("wromg age")
    else:
        print(" eligiable")
try:
    fun(1)
except Invalidage as e:
    print("erroe",e)
    


