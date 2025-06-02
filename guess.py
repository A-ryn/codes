import random
lown=1
highn=10
num=random.randrange(lown,highn)
gameon=True
count=0
while gameon:
    guess=int(input("guess the number"))
    if guess==num:
        print("won")
        count=count+1
        gameon=False
    elif guess!=num:
        print("ty again")
        count=count+1
       
    else:
        print("ivalid comment try input a number ")
