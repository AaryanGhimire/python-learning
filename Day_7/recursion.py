#When a function calls itself repeatedly,it is called recursion
#Recursive function
def show(n):
    if(n==0):#base case
        return
    print(n)
    show(n-1)
show(5) 

#factorial using recursion
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

#Write a recursive function to calculate the sum of first n natural numbers
def sum(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return n+sum(n-1)
    
print(sum(5))

#Write a recursive function to print all elements in a list
#hint:Use list &index as parameters
def print_list(list,index=0):
    if(index==len(list)):
        return
    print(list[index])
    print_list(list,index+1)

fruits=["mango","apple","banana"]
print_list(fruits)
mango=["good","riped","rotted"]
print_list(mango)