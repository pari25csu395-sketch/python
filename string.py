str1 = "This is a string."

str2 = "My name is Pari. \nI am in second year of btech." #\n is for next line. , \t is for tab space.

print(str2)

#concatenation of strings

str3 = "Pari"
str4 = "Aggarwal"

str5 = str3 + " " + str4
print(str5)

#length of string

length = len(str1)
length2 = len(str2)

print("The length of str1 is: ", length)
print("The length of str2 is: ", length2)

#indexing of string , it starts from 0.

ch = str3[2]
ch1 = str4[0]

print(ch)
print(ch1)

# slicing of a string

print(str5[ : len(str5)]) # 0:13
print(str5[-8 : -1]) # 5:12 last se ek phle tk hota h print
