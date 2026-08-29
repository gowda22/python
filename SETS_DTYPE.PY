set1={'a','b','c',2,3,"hello",True,1,"false"}
print(set1)
print(type(set1))

# # #ADDING ITEAM
# # set1.add("false")
# # set1.add("heuu")
# # set1.add("heuu")
# # print(set1)

# # #UPDATE
# # set1.update([1,2,3,4])
# # print(set1)

# # #REMOVING THE ITEAM

# # set1.remove("false")
# # print(set1)#it give err iif not


# # #DISCARD

# # set1.discard(True)#not give erros if not present
# # print(set1)

# # set1.clear()
# # print(set1)

# # DEL 
# # set1 = {10, 20, 30, 40}

# # print(set1)

# # del set1

# # print(set1)



# #SETS OPEARATIONS

# #UNION
# set1={1,2,3}
# set2={3,4,5}
# print(set1.union(set2))
# print(set1|set2)

# #INTERSECTION

# # set3=(set1.intersection(set2))
# # print(set3)

# # set1.intersection_update(set2)
# # print(set1)

# #DIFFERENCE

# # set4=set1.difference(set2)
# # print(set4)
# # set1.difference_update(set2)
# # print(set1)

# #SYMETRIC DIFFERENCE{non unic}
# # set3=set1.symmetric_difference(set2)
# # print(set3)
# # set1.symmetric_difference_update(set2)
# # print(set1)


# #SUB SET

# a={1,2}
# b={1,2,3}
# print(a.issubset(b))
# print(a.issuperset(b))




#frozen set

# fs=frozenset([1,2,3,4]) #store dict key
# print(fs)
# print(type(fs))

#TO CHEK ITAM{ in}

print("hello" in(set1))
#rturn true

