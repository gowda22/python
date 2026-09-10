def prime(n):
    if n<=1:
        return "not prime"
    for i in range(2,n):
        if i%2==0:
            print( "not prime")
            return 
        print("prime")

num=int(input("enter no:"))
prime(num)


        
        