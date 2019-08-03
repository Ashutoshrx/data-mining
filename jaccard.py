list1=[]
list2=[]

for i in range(2):
    x=int(input("Enter the nums for list 1:"))
    list1.append(x)

for i in range(2):
    y=int(input("Enter the nums for list 2:"))
    list2.append(y)
#print(list1)
#print(list2)

def findindex(lst,val):
    return [i for i,x in enumerate(lst) if x==val]

a=findindex(list1,1)
print("Indices of 1s in list1="+str(a))
b=findindex(list2,1)
print("Indices of 1s in list2="+str(b))
c=findindex(list1,0)
print("Indices of 0s in list1="+str(c))
d=findindex(list2,0)
print("Indices of 0s in list2="+str(d))

list3=[]
def common(l1,l2):
    l3=(set(l1).intersection(set(l2)))
    count=len(l3)
    return count

commom1=common(a,b)
common0=common(c,d)
print("Number of 1s in common:"+str(commom1))
print("Number of 0s in common:"+str(common0))

num= common(a,b)
print("numerator:"+str(num))
den=len(list1)-common(c,d)
print("denominator:"+str(den))
jaccard=float(num/den)
print("THE JACCARD IS:"+str(jaccard))








