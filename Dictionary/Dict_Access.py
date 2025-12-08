my_dict={'name':'vanshi', 'age':27}
print(my_dict['name'])

#AGR VALURE NHI HAI TO KEY ERROR AAEGA
# print(my_dict['address'])

#using .get()
print(my_dict.get('age'))

#.get function agr value exixt nhi karti to none print karega error nhi aaega
print(my_dict.get('address'))

my_dict['name']='alshifa'
print(my_dict)

#add new key
my_dict['degree']='M.tech'
print(my_dict)