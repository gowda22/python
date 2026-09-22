# #myltithreading {running multi prog parallely}
# #we use threading module and we have main thread and child thread
# import threading
# import time
# def numbers():
#  for i in range (1,6):
#     print(f"numbers",i)
#     time.sleep(1)

# def letters():
    
#     for  j in ["a","b", "c","d","e"]:
#         print(f"letters",j)
#         time.sleep(1)


# #creating thread 
# t1=threading.Thread(target=numbers)
# t2=threading.Thread(target=letters)
# #starting thread
# t1.start()
# t2.start()

# #join used to print after competion of execution
# t1.join()
# t2.join()
# print("program is completed")



# multithraeding using arguments
import threading
import time
def greet(name):
   for i in range(1,4):
      print(f"hello {name} count{i}")
      time.sleep(1)
def animal(name):
   for i in range (1,6):
      print(f"this is {name} count{i}")
      time.sleep(1)
#creating thread 
t1=threading.Thread(target=greet,args=("alan",))

t2=threading.Thread(target=animal,args=("monkey",))
t3=threading.Thread(target=greet,args=("bob",))
t1.start()
t2.start()
t3.start()

