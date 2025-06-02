key=7
list=[1,2,7,4,5,6]
n=len(list)-1
def find(k,l,n):
    if list[n]==key:
        return "keyfound"
    else:
        return find(k,l,n-1)
print(find(key,list,n))