# #if con
# # age=(int(input("enter your age: ")))
# # if age>=18:
# #     print(" u r eligibal to vote:") 
# # else:#{if false it exicute this}
# #     prinjt(" not eligibal try after 18:")

# #QUES
# gender=input("enter ur gender:")
# regender=gender.lower()
# if gender==("male"):

#     print("you r male")

# elif gender==("female"):
#     print("u r female")

# else:
#     print("invalid ")


#If elif and else {mul posibalities}

# age=int(input(" enter ur age: "))
# if age<13:
#     print("child")
# elif age<18:
#     print("teenager")
# else:
#     print("adult")

#NESTED IF {IF IN ANTHER IF}
# age=int(input(" enter ur age: "))
# gender=input("enter ur gender:")
# if age>=18:

#     if gender.lower()=="male":
#         print("eligible to vote")
#     else:
#         print("not eligible")
# else:
#     print("not eligible to vote")

#GREATE OF 3NUM
n1=int(input("enter num 1: "))
n2=int(input("enter num 2: "))
n3=int(input("enter num 3: "))

if n1>n2 and n1>n3:
    print(f"num1 is greater {n1}")
if n2>n1 and n2>n3:
    print(f"num2 is greater {n2}")
else:
    print(f"num3 is greater {n3}")





