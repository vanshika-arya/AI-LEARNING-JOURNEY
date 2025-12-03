#numpy is an array -> numerical computation karte hain...fast way me...kisi value ko calcuate karke hme de date hain...it is a packgae jo c me banaya gya hai 
import numpy as np
a=np.array([0,1,2,3]) #numpy array banane ke liye np.array() use karte hain
print(a)

print(np.arange(10))

#why useful.....fast haiiiiiii 1000 times
# a=np.arange(1000)
# print(%timeit a**2) #jupyter notebook me chal rha hai....!!!!

#dimensions
print(a.ndim) # output 1 --> 1d array hai
print(a.shape) #output 4 --> 4 columns
print(len(a))

#2d array
b=np.array([[1,2,3],[5,6,7]])
print(b)
print(b.ndim) # output 1 --> 1d array hai
print(b.shape) #output 4 --> 4 columns
print(len(b)) #returns the size of the first dimensions

#multidimentional array
c=np.array([[[0,1],[1,2]],[[4,5],[9,8]]])
print(c.ndim) # output 1 --> 1d array hai
print(c.shape) #output 4 --> 4 columns
print(len(c))

d=np.arange(1, 10,2) #start, end(exclusive) ,step
print(d)

#linear space
f = np.linspace(0, 1 ,6) #start, end, number of parts jitne me divide karenge
print(f)

g = np.linspace(0, 1 ,10)
print(g)

#common arrays
a=np.ones((3,3)) #sare elements 1 honge 3*3 ka matrix
print(a)

b=np.zeros((10,6)) #sare elements 1 honge 3*3 ka matrix
print(b)

#identity matrix
c=np.eye(3)
print(c)

c=np.eye(3,2) #3 is no of rows and 2 is no columns
print(c)

#diagonal
c=np.diag([1,2,3,4])
print(c)
print(np.diag(c))

a=np.random.rand(4)
print(a)

b=np.random.randn(5) #return a sample(or smaples) from
print(b)

a=np.arange(10)
print(a.dtype)

#conevert in float
a= np.arange(10, dtype='float64')
print(a.dtype)

a=np.zeros((3,3))
print(a.dtype)
print(a)

#complex datatype
d = np.array([1+2j, 2+4j])
print(d.dtype)

e=np.array([True, False, True, False])
print(e.dtype)

s=np.array(['Ram', 'Robert', 'Rahim'])
print(s.dtype) #u aaega that means unicode (unicode is a string and 6 is the size)

a=np.arange(10)
print(a[5])
print(a[1:4])

a=np.diag([1,2,3])
print(a[2,2])

#assign value
a[2,2]=7
print(a[2,2])

a=np.arange(1,10,2)
print(a)


#we can also combine assignment and slicing
a=np.arange(10)
a[5:]=10 # index 5 ke baad ki sari value 10 ho jaengi
print(a)

b=np.arange(5)
a[5:]=b[::-1]
print(a)

f=np.arange(14)
b=f[::2] #2 2 ke step me print karega
print(b)

print(np.shares_memory(f,b))
b[0]=10
print(b)

print(np.shares_memory(f,b)) #ye bhi true aaega bczagr b me change karega to f me bhi change hoga
print(f)

c=f[::2].copy()
print(c)

print(np.shares_memory(f,c)) #copy banane pr wo different memory location pr cpoint  karega isliye false aaega

c=np.array([[[0,1],[1,2]],[[4,5],[9,8]]])
print(c.ndim) # output 1 --> 3d array hai
print(c.shape) #output 4 --> 4 columns
print(len(c))