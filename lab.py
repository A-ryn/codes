def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
       return fib(n-1)+fib(n-2)
    
num=int(input("enter the limit"))
print(fib(num)) 
for i in range(0,num+1):
    print(fib(i))