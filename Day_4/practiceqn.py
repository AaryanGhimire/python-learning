#WAP to ask the user to enter names of their 3 favorite movies and store them in a list
list=[]
store=str(input("Enter you first favourite movie"))
list.append(store)
store=str(input("Enter you second favourite movie"))
list.append(store)
store=str(input("Enter you third favourite movie"))
list.append(store)

print(list)

#WAP to check if a list contains a palindrome of elements.
#palindrome means same from front and back like "maam","nayan","racecar"
list=[1,2,3,2,1]
newlist=list.copy()
newlist.reverse()
if(list==newlist):
    print("palindrome")
else:
    print("not palindrome")

#WAP to count the number of students with the "A" grade in the following tuple
#["C","D","A","A","B","B","A"]
tup=("C","D","A","A","B","B","A")
print(tup.count("A"))

#WAP to store ["C","D","A","A","B","B","A"] in a list and sort them from A to D
grade=["C","D","A","A","B","B","A"]
grade.sort()
print(grade)