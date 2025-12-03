import numpy as np
#basic operations

a=np.array([1,2,3,4,5])
print(a+1)  #vectorization--> koi bhi operation perform ho...without any loop pure array me hoga....numpy ka power(vectorization)

#power 2
print(a**2)

b=np.ones(5)+1 #b--> 2,2,2,2,2
print(a-b)
print(a*b)

#matrix multiplication
c=np.diag([1,2,3,4])
print(c*c)
print("-------------")
print(c.dot(c))

#comparison true false
a=np.array([1,2,3,4])
b=np.array([5,2,7,4])
print(a == b)
print(a> b)

#array wise comparison
a=np.array([1,2,3,4])
b=np.array([5,2,7,4])
c=np.array([1,2,3,4])
print(np.array_equal(a,b)) #false-->kyuki a or b ki value same nhi hai
print(np.array_equal(a,c)) #true --> kyuki a or c ki value same hain sari values

#logival operations
a=np.array([1,0,0,1], dtype=bool)
b=np.array([0,0,1,1], dtype=bool)
print(np.logical_or(a,b))
print(np.logical_and(a,b))
print(np.logical_not(a,b))

#transcendental Functions
a=np.arange(5)
print(np.sin(a)) #a ke andr jite value hai unka sine nikala hai example sin(1),
print(np.cos(a))
print(np.tan(a)) 
print(np.log(a))
print(np.exp(a)) #evaluates e^x for each element in a given input--> to grow an exponential  number very fast

#shape mismatch
a=np.arange(4)
# print(a+np.array([1,2])) #error -->operands could not be broadcast together with shapes (4,) (2,)
print(np.sum(a))

#sum by rows and columns
x= np.array([[1,1],[2,2]])
 
#column first dimension
print(x.sum(axis=0))

#row second dimension
print(x.sum(axis=1))

print(x.min())
print(x.max())

#min and max value ka index print karega
print(x.argmin())
print(x.argmax())

#logival operations
a=np.all([False,True,False]) #all check karega all value true hai ya nhi..
a=np.any([False,True,False]) #any check karega agr koi bhi ek value ture hai ya nhi...

a=np.zeros((50,50))
print(np.any(a!=0))

print(np.all(a==a))

a=np.array([1,2,3,4])
b=np.array([5,2,7,4])
c=np.array([8,0,9,4])
print(((a<=b)&(b<=c)).all())

x=np.array([1,2,3,4])
y=np.array([[1,2,3],[2,3,4]])
print(x.mean())
print(np.median(x))
print(np.median(y,axis=-1)) #last axis
print(x.std()) #full population standard dev

data=np.loadtxt('populations.txt') #load data into array object
print(data)

              