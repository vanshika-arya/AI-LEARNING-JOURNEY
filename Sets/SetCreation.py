s={1,2,3}
print(s)
print(type(s)) 

#set does not reapet the values -> duplicates are not allowed in sets (mutable values add kar sskte hain but duplicate value add nhi kar sakte)
s2={1,2,3,4,3,2,1}
print(s2)

#ek list duplicates contain kar sakti hai but agr use set me convert karke print kare to duplicates remive ho jaenge
s3 =set([1,2,3,4,2,3,5])
print(s3)

s4= set()
print(s4)

#set indexing support nhi karta
#print(s[1]) #error aaega