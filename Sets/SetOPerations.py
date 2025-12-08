#union of sets -> | operator
s1={1,2,3,4}
s2={2,3,4,5,6,7}
print(s1 | s2)

#union with union function
print(s1.union(s2))

#intersection _> & operator
print(s1 & s2)

#intersection -> intersection function
print(s1.intersection(s2))

#difference _> - operator
print(s1 - s2)

#with diffrence function
print(s1.difference(s2))

#symmentric difference -> jo value s1 me ho pr s2 me nhi and jo value s2 me ho but s1 me na ho...wo values print karega
print(s1 ^ s2)

#with symmetric_difference function
print(s1.symmetric_difference(s2))

#find subset
x ={"a","b","c","d","e"}
y ={"c","d"}
print(x.issubset(y)) #false bcz x ke sare elemnets y me nhi hai
print(y.issubset(x)) #true bcz y ke all elements x me hai
