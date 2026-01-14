from numpy import average

"""

# Basic List Operations

lst=[1,2,3,4,5]
fst=lst[0]
last=lst[-1]
len=len(lst)
print(fst,"\n",last,"\n",len)

lst=[1,2,3,4,5]
sum=sum(lst)
print(sum)
print(average(lst))

fruit=["apple","Banana"]
fruit.append("Orange")
fruit.insert(1,"papaya")
print(fruit)

fruit.remove("Banana")
fruit.pop()
print(fruit)

numlst=[0,1,1,2,3,4,5,5,5,6,7,8,8,9]
print(numlst.count(5))

#Search and Sorting

numlst=[0,1,1,2,3,4,5,5,5,6,7,8,8,9]
to_fnd=int(input("Enter a Number to Found"))
if to_fnd in numlst:
    print("NUmber Found at index ",numlst.index(to_fnd) )
else:
    print("Number not Present") 


numlst=[7,8,5,4,7,8,9,3,2,1,5,64,7,8,8,9]
lst=[0,1,2,3,4,5,6,7,8,9]
print(numlst)
lst.reverse()
print(lst)
numlst.sort()
print(numlst)
numlst.sort(reverse=True)
print(numlst)

"""

# Basic Tuple Operation

tup=(1,2,3,4,5,6)
print(tup[0])
print(tup[-1])
print(len(tup))

fruit=("apple","Banana","Papaya","Orange")
for i in fruit:
    print(i)
f_name=input("ENter Your Fruit Name")
if f_name in fruit:
    print("Fruit Found at Index",fruit.index(f_name))
else:
    print("Fruit Not Found")

concat=tup+fruit
print(concat)

# tuple Methods


numlst=(7,8,5,4,7,8,9,3,2,1,5,64,7,8,8,9)
to_fnd=int(input("Enter a Number to Found"))
if to_fnd in numlst:
    print("NUmber Found at index ",numlst.index(to_fnd) )
else:
    print("Number not Present") 
count=0
for i in numlst:
    if to_fnd==i:
        count+=1
    else:
        pass
print(to_fnd,"Found", count,"Times")

# Converstion and Nesting
numtup=(7,8,5,4,7,8,9,3,2,1,5,64,7,8,8,9)
print(numtup)
numlst=list(numtup)
for i in range(1,5):
    numlst.pop()
numlst.sort()
tup=tuple(numlst)
print(type(tup))
print(tup)

tup2=((1,2,2),(3,4,5))
for i in tup2:
    for y in i:
        print(y)
