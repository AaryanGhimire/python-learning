#for loop is used for sequential traversal. for traversing list, string, tuples etc
nums=[1,2,3,4,5]
for val in  nums:
    print(val)
tup=(1,2,3,4,5)
for num in tup:
    print(num)
str="Erling Braut Haaland"
for char in str:
    print(char)

#For loop with else
str="yo whats up?"
for char in str:
    print(char)
else:#works after loops end but doesnt work in break or continue
    print("END")
