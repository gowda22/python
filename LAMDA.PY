#LAMDA{A FUN WITHOUT NAME[LAMBA ARG:EXP]}

# product=lambda x,y:x*y
# print(product(3,5))

# square= lambda x:"even" if x%2==0 else "odd"
# print(square(5))

# #MAP FUNCTION{perfoem a fun on each element)
# list1=[1,2,3,4,5]
# res=list(map(lambda x:x**2,list1))
# print(res)

#FILTER(FILTER ELEMENT BASED IN CONDITION)
# list1=[1,2,3,4,5]
# res=filter(lambda x:x%2!=0,list1)
# print(list(res))


#SORTED {SORT IN ACCENDING BASEDE ON 1ST ELEMNT}{USE KEY}
# students = [
#     ("John", 80),
#     ("Alex", 95),
#     ("Sam", 70)
# ]

# result = sorted(students, key=lambda x: x[1])#ACC 
# # result = sorted(students, key=lambda x: x[1], reverse=True)#DEC

# print(result)

#REDUCE{ COMBINJE THE ELEMENT REPEATEDLY UNTILL 1 FINAL VAL REMAINING}
# import functools
# list1=[1,2,3,4,5]
# result=functools.reduce(lambda x,y:x+y,list1)
# print(result)

#RECURTION{CALL IT SELF}
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))

#exp
def count(n):
    if n==0:
        return
    
    print(n)
    count(n-1)
count(5)
