def gcd(a,b):
    if b==0:
     return a
    else:
       return gcd(a,a%b)
    
num=int(input("enter the number"))
num2=int(input("enter the number"))
print(gcd(num,num2))    