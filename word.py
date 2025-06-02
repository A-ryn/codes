import random 
password=(input("entert the password"))
l1=10**(len(password)-1)
l2=(10**(len(password)))-1
cont=True
se=[]
while cont:
    guess=random.randrange(l1,l2)
    if guess==int(password) and guess not in se:
      print(password," match: ",guess)
      cont=False
    else:
      print(password,"not match: ",guess)
       
    se.append(guess)    