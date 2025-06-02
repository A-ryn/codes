import random
deck={"1":"stone","2":"paper","3":"sisor"}
print('''
  ..........controls..........
  .     stone ; 1            .
  .     paper ; 2            .
  .     sisor ; 3            . 
  ............................       
      ''') 
gameon=True
while gameon:
    player_move=(input("you move"))
    pc_move=random.randrange(1,3)
    print(deck[f"{pc_move}"])
    if player_move==pc_move:
        print(f"you:{player_move}:  :{pc_move}opponent")
        print("draw")
    elif player_move==1 and pc_move==2:
       print(f"you:{player_move}:  :{pc_move}opponent")
       print("you lost")
    elif player_move==2 and pc_move==1:
        print(f"you:{player_move}:  :{pc_move}opponent")
        print("you lost ")
    else:
        print("error")   
  