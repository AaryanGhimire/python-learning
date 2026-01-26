#writing and appending in a file

f=open("demo.txt","w")
f.write("I want to learn javascript tommorow .Yo 123")#completely overwrites
f.close()
#"w" means overwriting whole text not adding whereas appending means adding to it
f=open("demo.txt","a")
f.write("Then i might move to ReactJS")#adds to that txt
f.close()

f=open("sample.txt","w")# or in "a" mode also
f.write("this was created by  w mode")
f.close()
#write and append can also create a file if the file doesnt exists

#with syntax
with open("demo.txt","r") as f:
    data=f.read()
    print(data)
#we dont need to close file while using with syntax it automatically closes it

#Deleting a file
#using OS module
#Module(like a code libarary)
import os
os.remove("sample.txt")