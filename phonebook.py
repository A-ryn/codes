run=True
telephone_directory={}
while run:
 def add_contact():
    key=input("name:")
    if key  in telephone_directory.keys():
      print("person already exist ")
    else:
       value=int(input("mobile number"))
       return telephone_directory.update({key:value})   
 def update_contact():
    key=input("name of persons no to be updated:")
    
    if key  in telephone_directory.keys():
      value=int(input("entert the new mobile number"))
      return telephone_directory.update({key:value})
    else:
       print("id not found")   
 def delete_contact():
    key=input("name of persons no to be deleted:")
    if key  in telephone_directory.keys():
      return telephone_directory.pop(key)
    else:
       print("person dosent exist ")    
 def search_contact():
    key=input("name:")
    if key  in telephone_directory.keys():
     return telephone_directory[key]
    else:
       return "id not found"
 def display_all_contacts():
    return telephone_directory 
 comand=int(input(""" 
      add a contact 1
      update a contct 2
      delete a contact 3
      search for a contact 4
      display all contact 5
      any other number to stop
      
      """))
 if comand==1:
   d=add_contact()
   print(telephone_directory)
 elif comand==2:
    update_contact()
 elif comand==3:
    delete_contact()
 elif comand==4:
    print("no:",search_contact())
    
 elif comand==5:
    print(display_all_contacts())
 else:
    run=False




    
    