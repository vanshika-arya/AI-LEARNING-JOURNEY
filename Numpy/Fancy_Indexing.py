import numpy as np
a=np.random.randint(0,20,15) #0 se 20 ke beech me  se 15 random value generate hongi 
print(a)

mask= (a%2==0)
print(mask)  #output true false me aagea even hai to true odd hai to false

extact_from_a = a[mask]
print(extact_from_a) #jitne even numbers hain wo print ho jaega

a[mask]= -1
print(a) #a[mask ] me jha bhi even number wha -1 aa jaega


a=np.arange(0,100,10)
print(a)

#access through indexing...index number may be repeated
print(a[[2, 3, 2, 4, 2]])

#new value may be assigned
a[[9,7]] = -200 #9 and 7th index pr -200 aa jaega
print(a)

