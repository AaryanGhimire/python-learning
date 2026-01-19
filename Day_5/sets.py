#Collection of unorderd items
#Each elements in the set must be unique and immutable
#Set can never store LIST and DICTIONARY because they are muttable
collection={1,2,3,4}
print(collection)
print(type(collection))
dupl={1,1,1,1,2,2,2,2,333,333,455,665}
print(dupl)#set ignores duplicate values ie items is {1, 2, 455, 665, 333} and also we can see it is unordered

empt=set()#syntax of empty set

#*****IMPORTANT*****
#set is MUTABLE
#*BUT
#elements inside set is IMMUTABLE