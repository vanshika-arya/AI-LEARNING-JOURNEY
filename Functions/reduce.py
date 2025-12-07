product =1
lst =[1,2,3,4]
for num in lst:
    product*=num
print(product)
#with reduce
from functools import reduce
def multiply(x,y):
    return x*y
product=reduce(multiply, lst)
print(product)
