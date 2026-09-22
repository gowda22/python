"""
MAGICAL OR DUNDER  ARE SPECILA AND PRE DEFINED METHODS THAT PYTHON CALLS 
AUTOMATICALLY 
HELPS TO INTITIALIZE OBJ
REPRESNT OBJ AS STRING
COUNTROL OBJECT BEHAVIOUR

"""

# __INIT__ CONSTRUCTOR {CALLED AUTO MATICALLY WHN OBJ IS CREATED }
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(self.name,self.age)


# cl=Student("gowda",23)
# cl.display()

#__str__{what i want to display withiout calling}

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"student name is{self.name}, and age is {self.age}"
# s1=Student("gowda",23)
# print(s1) # we can print wht we want without any fun or method


#lenth {used to return length of a object}
        
# class Course:
#     def __init__(self,student):
#         self.student=student
#     def __len__(self):
#         return len(self.student)
# c1=Course("ghj")
# print(len(c1))

"""
name magling:is a mechanisam where python uses to prvent accesdentl access 
it apply only parivate variable double under score  

"""

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.__mar=marks
    def show(self):
        print(f" name is {self.name} and marks is {self.__mar}")
s1=Student("charlie",80)
s1.show()
print(s1.name)
print(s1._Student__mar) #margling name 