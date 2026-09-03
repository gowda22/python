# numbers = [1, 2, 3, 4, 5,6]
# # for i  in range(1,6):
# #     result = []
# # for i in i:
# #     result.append(i ** 2)
 
# # LIST COM
# # result=[ i**2 for i in numbers] 


# # print(result)
# # numbers = [1, 2, 3, 4, 5,6]
# # result=[]#odd
# # numbers = [1, 2, 3, 4, 5,6]
# # for i in numbers:
# #     if i % 2==0:
# #         result.append( "even")

# #     else:
# #         result.append("oodd")

# # print(result)
# # in list compraension
# result=["even" if i%2==0 else "odd" for i in numbers]
# print(result)


  
#PRINT VS RETURN
# def add(a,b):
#     print(a+b)
# x=add(22,44) #xis none
# y=x+5
# print(y)#here it give error

def add(a,b):
     return (a+b)
x=add(22,44) #xis none
y=x+5
print(y)
z=y+3
print(z)

