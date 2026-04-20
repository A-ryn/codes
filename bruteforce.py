   

def brute():
    password=str(input("enter the password "))
    pas=eval(password)
    l1=10**(len(password)-1)
    l2=(10**(len(password)))-1

    for i in range(l1,l2):
     if pas==i:
      print(password,"=",i,"password match")
      break
     else:
      print(password,"=",i,"no match") 
    again=input("check agin (yes/no)")   
    if again=="yes":
      brute()
    elif again=="no":
     print("thank you")
    else:
     print("wrong comand")
brute() 

     