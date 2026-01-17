#Accessing parts of a string
#its syntax is :
#str[starting index:ending index] and its not upto ending index its upto second last index
str="Aaryan Ghimire"
print(str[0:8])#Output is Aaryan G as the ending index is h 
print(str[:4])#[0:4]
print(str[5:])#[5:len(str)]

#python has a special feature as Negative index 
#APPLE
#-5-4-3-2-1
str="apple"
print(str[-5:-2])#gives App as ending is -2 ie l


