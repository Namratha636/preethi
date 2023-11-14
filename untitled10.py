import time
def linearsearch (a,key):
    n=len(a)
    for i in range(n):
        if a[i]==key:
            return i
        return -1
a=[12,13,15,67,36,89]    
start=time.time()
print("enter the list of array")
k=int(input("enter the elements to search"))
i=linearsearch(a,k)
if i==-1:
    print("successfull search")
else:
    print("unsuccessfull search to found at location:",i+1)
end=time.time()    
        
        