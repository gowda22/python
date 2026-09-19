# """
# EXCEPTION HANDLING:- used to handle exception that we get whn we do a progs
# syntax error:-before exicition 
# runtime error:-after the execution
# ex="zerodivisionerror","type error","name error"
# """
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("can not divide by zero")
# else:
#     print("no error")
# finally:
#     print("succesfull")

# try:
#     print(10+a)
# except TypeError:
#     print("enter crt data type")
# except:
#     print("other error")
# else:
#     print("no error")

# finally:
#     print("done....")


#EX
try:
    n1=int(input("enter no1:"))
    n2=int(input("enter no2: "))
    result=(n1+n2)
    print(result)
except TypeError:
    print("enter crt val: ")
except ValueError:
    print("invalid val")
else:
    print("no erros")
finally:
    print("done")




