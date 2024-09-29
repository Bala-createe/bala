
b=[[[[3,4,5],[7,8,9,[11,12,14]]]]]
print(b[0][0][1][3][-1])

a={"a":{"b":{"c":{"d":[1,2,3,4,5]}}}}
print(a["a"]['b']['c']['d'][0])

a={"a":1,"b":"test",'c':"Test4"}
a.pop('a')
a.popitem()
a.clear()
del a["b"]
print(a)

b={"a":1,"b":"test"}
b['c']="test2"
b.update({'c':"test3",'d':"Test6",'e':"test7"})
b['c']="test4"
print(type(a),type(b))
print(b['a'])
print(b.get('a'))
print(b.keys())
print(b.values())
print(b.items())

a={1,2}
b={1,2,3}

print(a.issubset(b))
print(a)
print(b)

print(a.pop())
print(a.remove(2))
print(a.discard(5))
a.clear()
print(a)

b=set()
a.add(5)
a.update((8,9,10))
c=a.union((12,13,14))
print(a,c)
print(type(a))
for i in a:
    print(i)
print(list(a)[0])

print("New Code")

#this is some new code
