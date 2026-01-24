#WAP to find the sum of first n natural numbers.(using while loop)
n=int(input("Enter the value of n:"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i+=1
print(sum)

#WAP to find factorial of first n numbers.(using for loop)
n=int(input("Enter the value of n:"))
fact=1

for i in range(1,n+1):
    fact*=i

print("factorial =",fact)