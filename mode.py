nums=[1,2,3,2,4,2,4]
mode=[]#most frequent element in array 
count=0
result=0
for i in range(0,len(nums)):
 count=0
 for j in range(0,len(nums)):
   if nums[i]==nums[j]:
    count=count+1
 mode.append(count)
 if result<count:
  result=count
  n=nums[i]
print("mode of the list ",nums)
print("is :",n)

