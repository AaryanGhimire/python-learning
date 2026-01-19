#Store following word meanings in a python dictionary:
# table:"a piece of furniture","list of facts&figueres"
#cat:"a small animal"
dictionary={
    "cat":"a small animal",
    "table":["a piece of furniture","List of facts & figures"]
}
print(dictionary)

#You are given a list of subjects for students.Assume one classroom is required for 1 subject.How many classrooms are needed by all students
#"python","java","C++","python","javascript","java","python","java","C++","C"
#-> mathematically we solve that python java C++ C and javascript ie 5 classrooms is needed ie set ko length ko count is number of classroom
subjects={"python","java","C++","python","javascript","java","python","java","C++","C"}
print("The number of classroom needed is",len(subjects))

#WAP to enter marks of 3 subjects form the user and store them in a dictionary.Start with an empty dictionary and add one by one.Use subject name as key and marks as value
marks={}
x=int(input("Enter physics marks:"))
marks.update({"physics":x})
y=int(input("Enter chem marks:"))
marks.update({"chemistry":y})
z=int(input("Enter math marks:"))
marks.update({"math":z})
print(marks)

