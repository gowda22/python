# def  desc(numbers):
#     result=[]
#     for i in range (len(numbers)):
#         for j in range (i+1,len(numbers)):
#             if numbers[i]<numbers[j]:
#                 numbers[i],numbers[j]=numbers[j],numbers[i]
#     return numbers

# # numbers=[23,54,55,44,22,]
# # print(desc(numbers))


# l1=[10,34,22]
# l1.sort(reverse=True)
# print(l1)

# numbers = list(map(int, input("Enter numbers: ").split()))

# result = sorted(numbers, reverse=True)



# print(result)
"============="

# numbers = input("Enter list: ").split()
numbers=[20,44,6,7,8,89]

result = sorted(numbers,reverse=True)
print(result[-2])


print(result)


"=="
n=int(input("enter no"))
for i in range (1,n):
    print(i )