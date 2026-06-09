str = "i am studying python."

print(str.endswith("on."))
print(str.capitalize()) #capitalizes the first letter of the string.
print(str) #no changes here

str = str.capitalize() #capitalizes the first letter of the string and assigns it back to str.
print(str) #changes are reflected here.

print(str.replace("python", "cpp")) #replaces "python" with "cpp" in the string.

print(str.find("am")) #finds the index of the first occurrence of "am" in the string.

print(str.count("t")) #counts the number of occurrences of "t" in the string.