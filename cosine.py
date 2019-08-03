import math
list1=[]
list2=[]
for i in range(4):
    x=int(input("Enter the inputs for list1:"))
    list1.append(x)

for i in range(4):
    y=int(input("Enter the inputs for list2:"))
    list2.append(y)

print(list1)
print(list2)

def dotproduct(l1,l2):
    if len(l1) != len(l2):
        return 0
    else:
        return sum(i[0] * i[1] for i in zip(l1, l2))
num=dotproduct(list1,list2)
print("The numerator is:"+str(num))

def findmodule(l1):
    sum = 0
    for i in l1:
        sum+=(i*i)
        sol=math.sqrt(sum)
    return sol

y=findmodule(list1)
z=findmodule(list2)
den=float(y*z)
#den=float(den)
print("The denominator is:"+str(den))
cosine=float(num/den)
print("The cosine similarity is:"+str(cosine))

