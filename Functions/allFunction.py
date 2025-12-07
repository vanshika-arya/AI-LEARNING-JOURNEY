#return value of all() function
#True: if all elements in an iterable are true
#False: if any element in an iterable is false
lst=[1,2,3,4]
print(all(lst)) #output true

lst1=[0,1,23]
print(all(lst1)) #output false

lst2=[False,-1,23]
print(all(lst2)) #output false