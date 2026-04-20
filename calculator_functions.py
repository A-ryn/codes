def even(n):
 if n%2 == 0:
   print("even")
 else:
   print("odd")
def fact(n):
 if n == 0 or n == 1:
   return 1
 else:
    print(n*(n-1))

def prime(n):
  result="prime"
  for i in range(2,n):
     if n%i == 0:
       result="not prime"
       break
     else:
       pass
  print(result)

def cel(n):
 faren= (n*1.8)+32
 print(faren)


c=int(input(''' 1.  even  
                2.  factorial
                3. prime check 
                4  clecious to farenheit 
       eneter the choice : '''))
n=int(input("eneter the number"))
if c == 1:
 even(n)
elif c == 2:
 fact(n)
elif c == 3:
 prime(n)
elif c == 4 :
 cel(n)
else:
 print("wrong command")

