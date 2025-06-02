def possibile(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return possibile(n-1)+possibile(n-2)  
    
n=int(input("enter the length of list")) 
print(possibile(n),"ways are possible" )   
