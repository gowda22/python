L1=["hello", "hio",1,2,[1,2,3], True]

#append
L1.append("banglore")
print(L1)

# insert

L1.insert(2,60)
print(L1)

#EXTENDS add iteam with itearable

L2=[1,2,3,4,5,6,]
L1.extend(L2)
print(L1)
print(L2)



#REMOVEING THE METHODS IN LIST

#REMOVE
L1.remove("hio")
print(L1)

# #pop[indeex]

rem=L1.pop(3)#REMOVE AND RETUN 
print(L1)
print(rem)

#clear [delete all]
L2.clear()
print(L2)


#DELETE ENTIRE LIST GIVE ERROR TRY TO PRINT
# del L1
# print(L1)

#MOIFTY EXSISTING

L1[1]="gowdaaa"#at index 1 it change

print(L1)
print(len(L1))