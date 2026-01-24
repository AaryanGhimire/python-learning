#learning about range function
print(range(10)) #output is range(0,10)
#now
sequence=range(10)
for i in sequence:
    print(i) #prints the range from 0 to 9(range-1)

#*****IMP******
#Range includes three parts ie (start,stop,step)
#*********************************************
for i in range(10):# range(stop) here start is default 0 and step is default 1
    print(i)
for i in range(2,10): #range(start,stop) step is default 1
    print(i)
for i in range(2,10,2): #range(start,stop,step) everything is given
    print(i)