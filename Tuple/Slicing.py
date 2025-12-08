t=1,2,3,4,5,6,7
print(t[1:4])

#print elements from starting to 2nd last element
print(t[:-2])

#print elements from starting to end
print(t[:])

#tuple ki value ko chnage nhi kar sakte
t1=(1,2,3,4,[4,5,6],8)
t1[4][1]='vanshika' # tuple ke 4th index pr list hai or uske 1 index pr hum value insert kar rhe.....list me hum value chnage kar sakte hain 
print(t1)
# t1[2]='x'  #error 'tuple' object does not support item assignment

#concatinating tuples
t=(1,2,3)+ (4,5,6)
print(t)

#repeatation in tuple
t=(('vanshi',)*4)
print(t)