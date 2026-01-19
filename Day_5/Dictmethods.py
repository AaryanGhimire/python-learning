student={
    "name":"Jon snow",
    "subjects": {
        "phy":97,
        "chem":98,
        "math":95
    }
} 
print(student.keys())#provides only keys (also no nested keys only student keys)
#we can typecast into list as well 
print(list(student.keys()))
print(student.values())#values of the dictionary(all including nested)
print(student.items())#all items key and value as dict_items([('name', 'Jon snow'), ('subjects', {'phy': 97, 'chem': 98, 'math': 95})])
#important
print(student["name"]) #ouptput jonsnow
print(student.get("name"))#output jonsnow #this is another method
#but if name2 
#print(student["name2"]) #ouptput error
print(student.get("name2"))#output no error->None
#this two is similar but we use methods for ease as it doesnt show error in long programs

student.update({"city":"kathmandu"})

print(student)