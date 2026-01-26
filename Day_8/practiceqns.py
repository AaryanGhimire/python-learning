#Create a new file "practice.txt" using python .Add the following data in it:
    # Hi everyone
    # we are learning file i/o
    # using java
    # i like programming in java
# f=open("practice.txt","a")
# f.write("\ni like programming in java")
#  f.close()

# WAF that replaces java with python in above file
# with open("practice.txt","r") as f:
#     data=f.read()
# new_data=data.replace("java","python")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)
    
#search if the word searching exists in the file
# word="learning"
# with open("practice.txt","r") as f:
#     data=f.read()
#     if(data.find(word)!=-1):
#         print("found")
#     else:
#         print("not found")

#WAf to find in which line of the file does the word "learning" occur first. print -1 if the word is not found
def check_for_line():
    word ="learning"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
                line_no=1
    return -1
print(check_for_line())    
#from a file containing numbers seperated by comma,print the count of even numbers