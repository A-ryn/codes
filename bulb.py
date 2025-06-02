onbulb=[]
for i in range(2,501):
    
    for j in range(i,501,i):
      if j not in onbulb:
       onbulb.append(j)
      else:
        onbulb.remove(j)

for k in range(0,len(onbulb)-1):
  print("the bulb",onbulb[k],"is on")