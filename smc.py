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
print("a1="+str(a))
b=findindex(list2,1)
print("b1="+str(b))
c=findindex(list1,0)
print("c0="+str(c))
d=findindex(list2,0)
print("d0="+str(d))

#print(list1)
#print(list2)
list3=[]
def common(l1,l2):
    l3=(set(l1).intersection(set(l2)))
    count=len(l3)
    return count

print(common(a,b))
print(common(c,d))
#if common(c,d)==0:
#    print(common(c,d))
#else:
#    print(int(common(c,d)+1))


num= common(a,b)+ common(c,d)
print("numerator:"+str(num))
den=len(list1)
print("denominator:"+str(den))
smc=float(num/den)
print("THE SMC IS:"+str(smc))








