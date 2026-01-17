#WAP to input users first name and print its length
name=input("Enter your first name:")
print("Its length is:",len(name))

#Wap to find the occurence of $ in the string
string=input("Enter a string")
print("The occurence of $ in the string is ",string.count("$"),"times")

#Wap to check if a number entered by user is odd or even
num=int(input("Enter a number: "))
if(num%2==0):
    print("even number")
else:
    print("odd number")

#Wap to find the greatest of 3 numbers entered by the user
num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
num3=int(input("Enter a number: "))
if(num1>=num2 and num1>=num3):
    print("Num1 is the greatest")
elif(num2>=num1 and num2>=num3):
    print("Num2 is the greatest")
else:
    print("Num3 is the greatest")

#Wap to check if a number is a multiple of 7 or not
num=int(input("Enter a number: "))
if(num%7==0):
    print("multiple of 7")
else:
    print("Is not a multiple of 7")

#Wap to find the greatest of 4 numbers entered by the user
#Wap to find the greatest of 3 numbers entered by the user
num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
num3=int(input("Enter a number: "))
num4=int(input("Enter a number: "))
if(num1>=num2 and num1>=num3 and num1>=num4):
    print("Num1 is the greatest")
elif(num2>=num3 and num2>=num4):
    print("Num2 is the greatest")
elif(num3>=num4):
    print("Num3 is the greatest")
else:
    print("Num4 is the greatest")
