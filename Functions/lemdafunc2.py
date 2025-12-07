#use with filter function
lst = [1,2,3,4,5]
even_lst= list(filter(lambda x: (x%2==0),lst))
print(even_lst)

#use with map
new_lst = list(map(lambda x: x**2, lst))
print(new_lst)

# with reduce
# produce_lst = reduce(lambda x,y : x*y , lst)
# print(produce_lst)

#addition of two numbers
double = lambda x,y : x+y
print(double(3,5))

#sum of digits
sum_of_digits = lambda n: sum(int(digit) for digit in str(n))
print(sum_of_digits(789))
    



