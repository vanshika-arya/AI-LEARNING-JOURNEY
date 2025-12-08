d={'a':1,'b':2,'c':3,'d':4}
for pair in d.items(): 
    #d.items -> list deta hai items ki
    print(pair)

#comprehension me loop ek hi line me likhte hai---kya karna hai---kis pr karna hai---kaise karna hai
new_dict={k:v for k, v in d.items() if v>2}
print(new_dict)

#operations on key and value
d={k +'c' : v*2 for k,v in d.items() if v>2}
print(d)