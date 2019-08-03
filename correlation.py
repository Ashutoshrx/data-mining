import math
list1=[]
list2=[]
for i in range(8):
    x=int(input("Enter the x cords:"))
    list1.append(x)

for i in range(8):
    y=int(input("Enter the y coords:"))
    list2.append(y)
print(list1)
print(list2)


sum_x=sum(list1)/len(list1)
#print("sum_x:"+str(sum_x))
sum_y=sum(list2)/len(list2)
#print("sum_y:"+str(sum_y))

list3=[]
for i in list1:
    x_bar=i-sum_x
    list3.append(x_bar)
print(list3)

list4=[]
for i in list2:
    y_bar=i-sum_y
    list4.append(y_bar)
print(list4)

def prod(a,b):
    p=[]
    for i in range(len(a)):
        p.append(a[i]*b[i])
    return p
numerator=sum(prod(list3,list4))
print("The numerator is:"+str(numerator))

def square(a):
    q=[]
    for i in range(len(a)):
        q.append(a[i]*a[i])
    return q
list5=square(list3)
#list5.append(square(list3))
print(list5)
list6=square(list4)
print(list6)

ashu=sum(list5)
#print(ashu)
tosh=sum(list6)
#print(tosh)
denominator=math.sqrt(ashu*tosh)
print("The denominator is:"+str(denominator))
coefficient=numerator/denominator
print("The CORRELATION COFFECIENT IS: "+str(coefficient))




