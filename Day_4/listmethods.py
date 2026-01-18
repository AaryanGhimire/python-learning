#Its like functions but are methods only for list
list=[2,1,3]
list.append(4) #adds value at the end ie[2,1,3,4]
print(list)
list.sort()#sorts in ascending order ie[1,2,3]
print(list)
list.sort(reverse=True)#sort in descending order ie[3,2,1]
print(list)
#in string first alphabet sorts
mandemn=[2,7,9,3]
mandemn.reverse()#Reverses the whole list
print(mandemn)
mandemn.insert(1,4)#insert element at index works like append but at certain index provided ie syntax is list.insert(index,value)
print(mandemn)
newlist=[2,1,3,1]
newlist.remove(1)#removes the first occurence of element ie[2,3,1] the first 1 is only removed not all 1 
print(newlist)
newlist.pop(1)#removes element in index ie syntax is list.pop(index)
print(newlist)

