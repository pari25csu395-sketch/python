# lists are mutable

marks = [99,89 , 77 , 23 , 45]
print(marks)
print(type(marks))

marks.sort() #sorts the list in ascending order
marks.sort(reverse=True) #sorts the list in descending order

print(marks[1:4])
print(marks[-4:])

print(len(marks))
print(marks[0])

student = ["Pari", 18, 100.34]
student[0] = "Ishaan"

student.append("London") #adds element at last
student.insert(1, "Aggarwal") #inserts element at index 1
student.remove(100.34) #removes the element 100.34 from the list
student.pop(0) #removes the element at index 2
student.reverse() #reverses the list


print(student)

