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
try:
    with open("sam.txt","r") as file:
        print(file.read())
except FileNotFoundError :
    print("file not found")
