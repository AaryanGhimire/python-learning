#There are generally two types of Function
# 1)Built-in function
    # print()
    # len()
    # range()
# 2)User Defined function
#   defined by user ie calc_sum() anything can be made eg: calc_mul(),fact() etc.

#WAF to print the length of a list.(list is the parameter)
Mancity=["Haaland","foden","Cherki","Reijnders","Ait Nouri"]

def print_len(list):
    print(len(list))

print_len(Mancity)

#WAF to print the elements of a list in a single line(list in the parameter)
Mancity=["Marmoush","foden","Cherki","Reijnders","Ait Nouri"]
def print_list():
    for item in list:
        print(item,end="")

print_list(Mancity)

#WAF to find the factorial of n.(n is the parameter)
def fact(n):
    factorial=1
    for i in range(1,n+1):
        factorial*=i
    print(factorial)
    return(factorial)
fact(3)

#WAF to convert USD to NPR
def Converter(usd_val):
    npr_value=usd_val*113
    print(usd_val,"Usd value=",npr_value,"npr")
Converter(53)