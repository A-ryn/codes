students=[]
marks=[]
m=[]
a=0
mk=[]
n=int(input("enter the no  students"))
for i in range(n):
 name=input(f"entert the ame of students {i+1}:")
 students.append(name)
 mar=input("enter marks with space between them")
 marks=mar.split()
 m.append(marks)
print(marks) 
print(m)
for j in range(n):
 mk=m[j]
 for k in range(len(mk)):
   a=a+int(mk[k])
 avg=a/len(mk) 
 result=(students[j],avg)
 print(result)
 