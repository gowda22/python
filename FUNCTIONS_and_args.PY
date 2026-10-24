# # def greet(name, location):
# #     print(f"hello {name} ur from {location}")

# # greet("gowda", "banglore")

# # a=int(input("enter the a:"))
# # b=int(input("enter the b:"))
# # def sub(a,b):
# #     print(a-b)


# # sub(a,b)

# #ARGUMENTS AND PARAMETERS

# #positional arg
# # def sub(a,b):#chageing args val rev
# #     print(b-a)

# # sub(5, 50)

# # #keyword args
# # def greet(name, location):
# #     print(f"hello {name} ur from {location}")

# # greet("gowda", location="banglore")#position arg folloed by key args

# # #default args
# # def greet(name, location="banglore",):
# #     print(f"hello {name} ur from {location}")

# # greet("gowda") #it takes default value for 

# # def add(a,b,c=0):
# #     print(a+b+c)
# # add(5,6,7)
# # add(5,6)

# #variable length args

# # def add(*args):
# #     print(args)
    
# #     total=0
# #     for i in args:
# #         total+=i#SUM OF ALL ARG PRINT(SUM(args))
# #     print(total)
# #     print(type(args))
# # add(2,3)
# # add(2,3,4)
# # add()

# #VARIABLE LENGTH KEYWORD ARGS

# def greet(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")
# greet(name="gowda", location="banglore", age=25, gender="male")
# greet(name="gowda", location="banglore")
# # greet("gowda",laction="banglore")#error positional arg after keyword arg

#ALL IN 1
# def demo (a,b=0,*args,**kwargs):
#     print(a,b,args,kwargs)
# demo(1,2,3,4,5, name="gowda",age=12)

# def process(*args):
#     result = []

#     for i in args:
#         if i > 5:
#             result.append(i)

#     return result

# print(process(22, 3, 4, 66, 88))


# def fun(**kwarg):
#     print(kwarg)

# fun(name="gowda",age=22)

# def demo(a,b=0,*args,**kwargs):
#     print(a,b,args,kwargs)

# demo(1,2,3,4,name="gowda",age=22)
    
# def demo(*args,**kwargs):
#     print(" student name:",args[0])
#     print("age:",args[1])
#     print("sname:",args[2])
#     print("details",kwargs)
# demo("gowda",22, "fff",course="python",city="banglore")


# def add(a,b):
#     return a+b

# r=add(10,33)
# print(r)

def demo( **kwarg):
    print(kwarg)

demo(name="gowda",age=33)


