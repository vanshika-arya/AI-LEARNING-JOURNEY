# in keyword
lst =["one", "three", "two", "four"]
if "one" in lst: #in checks the value ki wo list se belong karti hai ya nhi
    print('ai')

#not in keyword
if "six" not in lst: #if element belong nhin karta list me
    print("ds")

#reverse the lst -> function
lst.reverse()
print(lst)

#list sorting ---> sorted function in assending order
lst2 =[2,7,4,6,5]
sorted_lst = sorted(lst2)
print(sorted_lst)

#revese ---->  decending order by default reverse  value false hoti hai isiliye wo assending order me print sort karta hai...jab value true karte hain to wo desending order me sort karta hai
rev_lst=sorted(lst2 , reverse=True)
print(rev_lst)

#sort function
lst2.sort() #usi list yani lst2 ki value ko sort karega assending order me...same list ke andar koi nyi list nhi banegi
print(lst2)

lst3=[1,3,4,"a", "s",8,5]
print(lst.sort())# error aaega -> bcz sort function different data types pr apply nhi hota

#list having multiple references
abc= lst2
abc.append(3)  #abc and lst2 dono same memory ko point kar rhe hain...isi liye dono same hi print karegnge
print(lst2)