s="vanshika "
print(s[1])
print(s[-1]) #prints the last character using negative indexing
print(s[2:5]) #slicing 2nd to 5th character 

# print(s[10]) #jo value exist nhi karti to----->try to access index out of range error aaega
# print(s[1.5]) #error --> string indices must be integer
#s[4]='v' #error ---> string object does not support item assignment bcz strings arfe immutable
#print(s)

#delete entire string
#del s
#print(s) #error --> s is not defined

#concate
s2="alshifa"
print(s + s2)
print(s * 3)