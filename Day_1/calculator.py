a=float(input("input a number"))
b=float(input("input another number"))
op=input("enter a operation(+,-,*,/)")
if op == "+" :
    result=a+b
elif op == "-" :
    result=a-b
elif op == "*" :
    result=a*b
else:
    result=a/b

print("Result",result)