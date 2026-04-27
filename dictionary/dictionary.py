d = {} #empty dictionary
student = {
    "name" : "Gaurav",
    "age" : 25,
    "grade" : "C"
}
print(student["name"]+"\n")

r = student.get("name4")
print(r)

p = student.keys()
print(p)

q = student.values()
print(q)

s = student.items()
print(s)
for student in s:
    print(student)

l1 ={"Gaurav":95 ,
     "Gurmeet" : 92 ,
    }
l2 = {"Devansh" : 89,
      "Harshit" : 85}
l1.update(l2)
print(l1)
