# #normal copy

# list1 = [1, 2, 3, [4, 5]]
# list2 = list1
# list2.append(6) 
# print(list1)
# print(list2)
# print(id(list1))#op {1,2,3[4,5] and same id}
# print(id(list2))

# #shallow copy

# import copy
# list1 = [1, 2, 3, [4, 5]]
# list2 = copy.copy(list1)
# list2.append(6)
# # list2[3].append(6)if we try to chnage nested original will also change
# print(list1)
# print(list2)
# print(id(list1))
# print(id(list2))

#deep copyy

import copy
list1 = [10, 20, 30, [40, 50]]
list2 = copy.copy(list1)
# list2.append(20)
list2[3].append(60) # not effect original complte indipendent
print(list1)
print(list2)



