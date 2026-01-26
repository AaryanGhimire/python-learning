#python can be used to perform operations on a file.(read and write data)
#Types of all files
# 1.Text files: .txt,.docx,.log etc
# 2. Binary files: .mp4,.mov,.png,.jpeg etc

f=open("demo.txt","r")
data=f.read()
print(data)
line1=f.readline()
print(line1)
print(type(data))
f.close()

#so this was read mode