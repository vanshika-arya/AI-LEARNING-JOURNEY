#adds counter to an iterable and returns it(indexing kahi se bhi strat kar skate hain)
numbers = [20,10,30,50]
for index, num in enumerate(numbers,20):
    print("index {0} has value {1}".format(index, num))