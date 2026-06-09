# tuples are immutable

tup = (1,) # for single element in tuple we have to put comma after the element otherwise it will be considered as int or string etc. and not as tuple.
tup1 = (3,5,8,2,5,1)
print(type(tup))
print(tup)

print(tup1.index(5)) #returns the index of the first occurrence of 5 in the tuple
print(tup1.count(5)) #returns the number of occurrences of 5 in the tuple