#method that dont use the self parameter (works at class level)
class Student:
    college_name="NCIT college"#class attr
    def __init__(self,fullname):
        self.name=fullname#obj attr
        print("adding  new student in Database")

    @staticmethod #decorator
    def hello():
        print("hello")

s1=Student("aaryan")
print(s1.name)

s2=Student("RN")
print(s2.name)

s2.hello()

#TWO PILLARS OF OOP
#1.ABSTRASCTION:hiding the implementation details of a class showing only essential features to the user
#2.ENCAPSULATION:wrapping data and functions into a single unit (object)
#3.INHERITANCE:
#4.POLYMORPHISM: