
b=list()
#single value
#a.insert(1,5)
#a.append(10)
#Multiple value
#a=a+[7,8]
#a.extend((8,9))
#a.pop(1)
#a.remove(1)
#del a[:2]
"""
a[2]=10
print(a)
a[1:1]=[11,12]
"""
a=[1,2,4,5,6,7,8,1,1]
print(a.count(1))
print(len(a))
print(a.index(1,3))
a.reverse()
a.sort(reverse=True)
b=a.copy()
c=a
print(a is b)
print(a is c)
print(a)

def getkey(a):
    return abs(a-50)
a=[15,35,42,62,51,61,75]
print(a)
a.sort(key=getkey,reverse=True)
print(a)


a=['a','A','b',"b","c","C"]
a.sort(key=str.lower)
print(a)

"""
Get 100 random numbers between 1 - 100
add it into list
if its a duplicate and dont add them
Once final list created Check for values divisible by 4 and remove them
if a value look like this 11 22 33 remove them as well.
Sort the values and get top 10 numbers and bottom 10 numbers
"""

import random
mylist=[]
for i in range(100):
    x=random.randint(1,100)
    print("Duplicat - ",x) if x in mylist else print("Divisible by 4",x) if x%4==0 else print("Divisible by 11") if x%11==0 else mylist.append(x)
mylist.sort(reverse=True)
print("Top 10 Items :", mylist[:10])
print("Bottom 10 Items : ",mylist[:-11:-1])