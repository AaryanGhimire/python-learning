collection=set()#empty set
collection.add(1)#adds element
collection.add(2)
collection.add("Hello")
collection.add((1,2,3))#can add tuples but NOT lists
print(collection)
collection.remove(1)#removes element
print(collection)
collection.clear()#empties the set
print(collection)
hello={"hi","hallo","ni hao"}
print(hello.pop())#randomly pops a value
#Sets union and intersections
set1={1,2,3}
set2={3,4,5}
print(set1.union(set2))#prints union
print(set1.intersection(set2))#print intersection
