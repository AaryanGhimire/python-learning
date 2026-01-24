#break is used to terminate loop when encountered
i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1

print("end of loop")
#continue is used to terminate execution of current execution and continue execution of loop with the next iteration
#for example
i=1
while i<=10:
    if(i%2==0):
        i+=1
        continue #it simply is skip as it skips print if (i%2==0)
    print(i)
    i+=1
