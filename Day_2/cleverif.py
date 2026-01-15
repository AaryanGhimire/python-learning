#this is clever if statement
#variable=(falsevalue,truevalue)[condition]
age=int(input("age:"))
vote=("nah you cant vote","yes can vote")[age>=18 and age<=59]
print(vote)
