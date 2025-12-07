lst =["three",1,2,3,4]
lst.insert(2, "three") #insert function tab use karte hain jab kisi specific position pr value add karna ho
print(lst) 

#remove ---> removes first occurance if there is duplicate value in the lst
lst.remove('three')
print(lst)

# concate...
lst2 = ["four","five"]
lst.append(lst2) # lst2 ke elments lst me add karega but ek nyi list banaega list ke anadr
print(lst)

lst.remove(lst2) #direct value de rhe hain jo hme delete karni hai
print(lst)

#extend function -> lst2 ke elements ko lst me hi dalega...koi dusri list nhi banaega
lst.extend(lst2)
print(lst)

#delete the element -> ye sidhe value del kar kar deta hai...ise variable me store nhi kar sakte
del lst[1] #pass index no. jisse value delete kar karni hai
print(lst) 

#pop....
a= lst.pop(1)  #pass index no. jiski value delete karni hai
print(a) #kon sa value delete kiya wo bta rha hai...iske through hum delete value ko ek variable me store kar sakte hain...taki hme pta chal jae exactly kon si value delete ho rhi hai
print(lst)