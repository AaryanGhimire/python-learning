#blocks of statements that perform specific tasks
#function definintions
def calc_sum(a,b):#parameters
    return a+b

sum=calc_sum(2,3)#function call;arguements
print(sum)
#Another example if no return then output will be none 
def print_hello():
    print("Hello")

output=print_hello()#output is hello
print(output)#output is none 

#avg of 3 numbers
def avg(a,b,c):
    return (a+b+c)/3
average=avg(2,3,5)
print(average)