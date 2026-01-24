#for loop practice qns
#print the elements of the followwing list using a for loop
    #[1,4,9,16,25,36,49,64,81,100]
# num=[1,4,9,16,25,36,49,64,81,100]
# for val in num:
#     print(val)
#Search for a number x in this tuple using loop:
    #[1,4,9,16,25,36,49,64,81,100]
tup=(1,4,9,16,25,36,49,64,81,100)
x=49
index=0
for val in tup:
    if(val==x):
        print("value found  at index",index)
        break
    index+=1
    print("finding")
else:
    print("END")