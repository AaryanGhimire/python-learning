age=int(input("age:"))
if(age>=18 and age<=59):
    print("Eligible for voting")
else:
    print("Not eligible for voting")

#Conditional statements consits of Indentation ie if paxi ko arko line ma 4 spaces xodna parxa format milna parxa

light=input("light color:")
if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("look")
elif(light=="green"):
    print("go")
else:
    print("The light is broken")

#single line conditional statements

food=input("food:")
eat="yes" if food=="cake" else "no"
print(eat)

#another format
food=input("food:")
print("sweet") if food=="cake" or food=="jalebi" else print("not sweet")