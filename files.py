f = open("filesdemo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()

# f.readline to print text line by line.

f = open("filesdemo.txt", "w") # w is fro remove the previous text and write a new text
data = f.write("I am sorry, i am learnin dsa.")
f.close()


f = open("filesdemo.txt","a") # a is to write after the existing text
data = f.write("and i am still going to kerala.")
f.close()

f = open("sample.txt", "w") # create a file 
f.close()

import os
os . remove("sample.txt") # to delete a file
