#Practice qn using for and range()

#print numbers from 1 to 100

for val in range(1,101,1):
    print(val)

#print numbers from 100 to 1

for value in range(100,0,-1):
    print(value)

#print the multiplication table for a number n
n=int(input("enter a number"))
for value in range(1,11):
    print(n*value)