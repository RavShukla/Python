students = ["Gaurav", "Gurmeet", "Devansh", "Udit", "Harshit"]
for student in students :
    print(student )

print("\n")
students.append("Vaibhav") #append method adds the element in list
students.append("Gaurav")
print("list after executing append function")
for student in students :
    print(student)

print("\n")
leet_students = ["Manasvi","Kanishka"]
students.extend(leet_students)#extend method adds two lists
print("list after executing extend function  ")
for student in students :
    print(student)

print("\n")
students.insert(1 , "Dipendra")
print("list after executing insert function")
for student in students :
    print(student)

print("\n")

stud =  students.pop(1)#pop methods pulls out the element from list
print(stud)
print("\n")

print("list after executing insert function")
for student in students :
    print(student)

print("\n")
indices = students.index("Gaurav")
print(indices)

print("\n")
ct = students.count("Gaurav")
print(ct)

print("\n")
st = students.sort()
for student in students :
    print(student)










