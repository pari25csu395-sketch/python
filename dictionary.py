info = {"name": "Alice", "age": 30, "city": "New York"}

print(info["name"])
info["name"] = "Bob"
info["surname"] = "Smith"
print(info)

#nested dictionary

student = {
    "name": "Alice",
    "age": 20,
    "subjects": {
        "math": 90,
        "science": 85,
        "java": 95
    }
}

print(student["subjects"]["java"])

print(list(student.keys())) # type casting to list to get the keys of the dictionary in a list format
print(len(list(student.keys()))) # to get the number of keys in the dictionary

pairs = list(student.items()) # to get the key-value pairs of the dictionary in a list format
print(pairs[0])

student.update({"age": 21, "city": "New York"}) # to update the value of age and add a new key-value pair city in the dictionary
print(student)

