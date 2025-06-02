class guy:
    def __init__(self,money,kal):
        self.money=money
        self.kal=kal
    def eat(self,food):
        if self.kal>=food:
            print("you won")
        else:
            print("you lost")
def gameover():
   return False          
def intro(gameon):
  start=(input("type s to start game  and n to stop game"))
  if start=="s":
    pass
  elif  start=="n":
     gameon=False
  else:
    print("type s to start ")
def gameplay(gameon):
   while gameon:
      player=input("enter the username ")
      gameon=gameover()
gameon=True
intro(gameon)
gameplay(gameon)





