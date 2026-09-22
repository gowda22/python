# """
# OPEN
# DO OPERACTION
# CLOSE
# """
# #OPEN A FIle and write {w}mood
# file=open("sample.txt","w")
# file.write("this is a 1st line\n ur in 2nd line")
# file.close()

# with open("sample.txt","w") as file:
#     file.write("gowdaa is a  good boy \n")
# with open("sample.txt","w") as file:
#     file.write("gowdaa is a  good boy \n")
    
    
# #opening file with read mood {r}

# file=open("sample.txt","r")
# content=file.read()
# print(content)
# file.close()
# with statement
# with open("sample.txt","r") as file:
#     print(file.read())
# with open("sample.txt","r") as file:
#     print(file.readline())
# with open("sample.txt","r") as file:
#     print(file.readlines())

# append file {a}
# file=open("sample.txt","a")
# file.write("this is a content by the append mood \n")
# file.close()

# #using with
# with open("sample.txt","a") as file:

#     file.write(" this is from append using with")

# FILE HANDLING WITH EXCEPTION
# try:
#     with open("sam.txt","r") as file:
#         print(file.read())
# except FileNotFoundError :
#     print("file not found")

# file=open("sample.txt","r")
# conten=file.read()
# print(conten)
# file.close()

# with open("sample.txt","r") as file:
#     print(file.read())


# with open("sample1.txt","w") as file:
#     file.write("this is neww file \n this is 2nd file")


class Invalidfiles(Exception):
    pass
def demo():
    try:

        with open("sample2.txt","r") as file:
            print(file.read())
    except FileNotFoundError: #u have to specify python buit in error
            raise Invalidfiles ("file not found")
try:
    demo()
except Invalidfiles as e:
    print("erroe",e)

class Invalid(Exception):
     pass
def age_chk(age):
     if age<18:
          raise Invalid("noo ur not eligiable")
     else:
          print(" u r eligiable")
try:
     age_chk(12)
except Invalid as e:
     print("error",e)

