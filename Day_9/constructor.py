#all classes have a function called init function which is initiated when object is called
class Student:
    college_name="NCIT college"#class attr
    def __init__(self,fullname):
        self.name=fullname#obj attr
        print("adding  new student in Database")

    def hello(self):#method requires self parameter
        print("hello")

s1=Student("aaryan")
print(s1.name)

s2=Student("RN")
print(s2.name)

s2.hello()