my_dict={'name':'vanshi' ,'age':27,'add':'buehra'}

#remove a particular item
print(my_dict.pop('age'))

print(my_dict)

#end se value delete kar dega pop item
my_dict.popitem()
print(my_dict)

squ={2:4, 3:9 ,4:16}
#delete particular key
del squ[2]
print(squ)

#remove all items
squ.clear()
print(squ)

#diclete whole dect
del squ
print(squ) #name error squ not defined