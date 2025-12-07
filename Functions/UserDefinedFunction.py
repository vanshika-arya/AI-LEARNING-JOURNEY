def addition(a,b):
    print (a+b)
def substraction(a,b):
    print (a-b)
def multiplication(a,b):
    print (a*b)
def division(a,b):
    print (a/b)
a= int(input())
b= int(input())
print("Option selection")
print("1. Addtion")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
c=int(input())
if(c==1):
    addition(a,b)
elif(c==2):
    substraction(a,b)
elif(c==3):
    multiplication(a,b)
elif(c==4):
    division(a,b)
else:
    print("invalid")
