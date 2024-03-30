'''
n=int(input("Enter a number"))
if n==0:
    print("Wrong Input")
else:
    for i in range(n,n+1):
        val=n*(n*1)
        print(val)
'''

'''
x=0
str1="thisismycountryindia"
for i in str1:
    x=x-1
    print(str1[0:x])
for i in str1:
    x=x+1
    print(str1[0:x])
'''

'''
n=int(input("Enter "))
x=0
str1="****************************************************************************************"
for i in range(n):
    x=x+1
    print(str1[0:x])
print("")
for i in range(n):
    x=x-1
    print(str1[0:x])
'''
'''
a1=1045
a2=format(a1,'b')
print(a2)
a1=1045
a2=format(a1,'d')
print(a2)
a1=1045
a2=hex(a1)
print(a2)
'''




'''
#accept an integer value and convert the string value into integer using int()
a=input("Enter the Integer")
b=int(a)
print(b,type(b))
'''

'''
#accept an integer value and convert the integer value into float using float()
a=int(input("Enter the Integer"))
b=float(a)
print(b,type(b))
'''

'''
#program to perform addition of strings and integer using explicit function
a=input()
b=int(input())
c=a+str(b)
print(c)
'''

'''
#Factorial of a number
a=int(input())
b=a
c=1;
for i in range(0,a):
    c=c*b
    b=b-1
print("Factorial is:",c)
'''

'''
# Program for printing "*" according to the given input

n=int(input("Enter number of astriks you need:"))
x=1
for i in range (n):
        print("*"*x)
        x=x+1
x=n-1
for i in range (n):
        print("*"*x)
        x=x-1
'''



