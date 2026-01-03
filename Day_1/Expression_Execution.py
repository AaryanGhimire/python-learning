
# this is single line comment
'''
This is a multi-line comment but pythons doesnt necesarrily have multiple line comments
or a docstring that's not assigned to anything,
so it works as a comment.
'''
#string and numeric values can operate together with * ie the outpuut =@@@@@@
A,B=2,3 
Txt="@" # string
print(2*Txt*3)

#String and string can operate using + ie output is 2@2@2@

C,D="2",3
Text="@"
print((C+Text)*D)

#Numeric values can operate with all arithematic operators output =14

A,B=2,3
C=4
print(A+B*C)

#Arithematic expression with integer and float will result in float output=50.0
A,B=10,5.0
C=A*B
print(C)

#Result of division operator with two integers will be float output=0.5
A,B=1,2
C=A/B
print(C)

#Integer division (//) with float and int will give int displayed as float ie if ans is 5 it will give 5.0
A,B=1.5,3
C=A//B
print(C,A/B)
# here output is C=0.0 and A/B=0.5
 
 #floor gives closest integer ,lesser than or equal to float value I REPEAT lesser 7.99 ko 7 hunxa not 8  and -5.2 ko -6 hunxa not -5

# Result of floor(A/B) is equal to Result of (A//B)

#Remainder is negative when denominator is negative 
A,B=-5,2
C=A%B
print(C)
# output =1
A,B=5,2
C=A%B
print(C)
# output =1
A,B=5,-2
C=A%B
print(C)
# output =-1


