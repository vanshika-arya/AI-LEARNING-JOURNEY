my_dict={'name':56}
squ={1:2, 3:4}
#cpoy karne ke liye
my_dict=squ.copy()
print(my_dict)

#fromkeys[seq[, v]]-> return a new dictionary with keys from seq and value
subjects ={}.fromkeys(['Math','English','Hindi'],0)
print(subjects)

subjects={2:4, 3:9, 4:16}
print(subjects.items()) #return a new view of dict items (key,value) tuple me show karega

#sirf key print karni ho
print(subjects.keys())

#sirf value print karni ho
print(subjects.values())

#to print all methods that can be performed on dict
d={}
print(dir(d))