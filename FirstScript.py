#loop
#condition based loop
#Iterator based loop
"""
a=1
while a<10:
    print(a)
    a=a+1

b="hello"
for i in b:
    if i=='l':
        break
    if i=='e':
        continue
    print(i)

a=2
for i in range(100):
    if i%a==0:
        print(i)
a=10**10

a="hello"
b="hello"

if not a==b and a!=b:
    print(True)
else:
    print(False)

#tomorrow task
a=11

#0-10 small 11-50 medium 50> large
if a>=0 and a<=10:
    print("Small number")
elif a>=11 and a<=50:
    print("Medium number")
elif a>=51:
    print("Large Number")

print("Small" if a>=0 and a<=10 else "medium" if a>=11 and a<=50 else "Large" if a>=51 else "") 

"""

#Guess Game, you need to take Guess from user 
a=input("Enter your guess (either o or e) : ")
if a=="o":
    print("odd")
else:
    print("even")

import random
num = random.randrange(1,100)
print(num)
if (a=='o' and num%2!=0) or (a=='e' and num%2==0):
    print("Win")
else:
    print("Lost")