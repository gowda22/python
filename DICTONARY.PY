# dict1={"name":"gowda","age":30,"location":"banglore"}
# print(dict1)
# print(type(dict1))

# # # #ACCESS KEY
# # print(dict1["age"])#if not give error

# # #GET METHOD acc val
# # print(dict1.get("name","name is not present"))

# # MODIFY EXSISTING DIC
# # dict1["age"]=25
# # print(dict1)

# #REMOVE ITEAM
# # x=dict1.pop("location")
# # print(dict1)
# # print(x)# retuen pop ele

# #add new key val
# dict1["gmail"]="gowda@123.com"
# print(dict1)

# #dict methoods
# #KEY
# print(dict1.keys())

# #val
# print(dict1.values())

# #iteams
# print(dict1.items())

# #DEL
# # del dict1
# # print(dict1)

# del dict1["age"]# perticular
# print(dict1)

# #clear
# # dict1.clear()
# # print(dict1)

# #update
# dict1.update({"email":"abc@11","gender":"male"})
# dict1.update({"email":"abc@11","gender":"femail"})#mod
# print(dict1)


#nested dict

students={"student1":{
    "name":"gowda",
    "age":44,
    "gender":"male"},

"student2":{
    "name":"harshaa",
        "age":34,
        "gender":"trans"}}

print(students["student2"]["gender"])#to acc




