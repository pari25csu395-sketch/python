# sets is unique and unordered collection of items. 
# they are immutable and cannot be changed once created. 


collection = {1,2,2,3,4,5, "hello", "world", 3.14, True, None }

print(collection)
print(type(collection)) 
print(len(collection)) # to get the number of items in the set , ignore duplicate items

emp_set = set() # to create an empty set 
emp_set.add(1)
emp_set.add(2) 
emp_set.add(2)
emp_set.add("hello ")

print(emp_set) 

emp_set.remove (2) # to remove an item from the set 
print (emp_set) 

print(emp_set.pop()) # to remove a random item from the set 

emp_set.clear() # to remove all items from the set
  
print(len(emp_set)) # to get the number of items in the set 


# SET UNION AND INTERSECTION 

set1 = {1,2,3,4,5} 
set2 = {4,5,6,7,8} 

print(set1.union(set2))

print(set1.intersection(set2))