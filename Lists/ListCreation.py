empty_list= []
lst =['one' ,'two', 1.8,5,True] #list of different datatypes
lst2 = [[1,2] ,[3,4]] #listof lists
print(empty_list)
print(lst2)
# process -> breack down in tokens....AST tree formation....byte code that is used (tab karega jab koi change karke code save hoga)
print(lst)

#length of list -> len() funtion...but how it works????
print(len(lst))

#list append -> append() function adds item in the list (new value) in the "END" of the list
lst.append(1.24) #intenally ek new list banegi jisme list ki copy banegi and new value bhi add ho jaegi and purani list ki memory free ho jaegi
print(lst)

del(lst[2])
print(lst)