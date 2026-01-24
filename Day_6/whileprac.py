# #********Practice qns using while loop*****************
# #print numbers from 1 to 100
i=1
while i<=100:
    print(i)
    i+=1
# #print numbers from 100 to 1
i=100
while i>=1:
    print(i)
    i-=1
#print the multiplication table of a number n
n=int(input("Enter a number :"))
print("The multiplication table of",n,"is:")
i=1
while i<=10:
    print(n*i)
    i+=1
#Print the elements of following list using a loop:
    #[1,4,9,16,25,36,49,64,81,100]
nums=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(nums):
    print(nums[i])
    i+=1
#Search for a number x in this tuple using loop:
    #[1,4,9,16,25,36,49,64,81,100]
tup=(1,4,9,16,25,36,49,64,81,100)
x=int(input("enter the number you want to search that is in tuple ie (1,4,9,16,25,36,49,64,81,100):"))
i=0
while(i<len(tup)):
    if(tup[i]==x):
        print("found at index",i)
    else:
        print("finding")
    i+=1
