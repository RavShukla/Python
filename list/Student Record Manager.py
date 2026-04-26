students = []

def AddStudent():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students.append([name, marks])


def ViewStudents():
    if len(students) == 0:
        print("No students available")
    else:
        for s in students:
            print("Name:", s[0], "| Marks:", s[1])


def DeleteStudent():
    name = input("Enter student name to delete: ")
    found = False

    for s in students:
        if s[0].lower() == name.lower():
            students.remove(s)
            print("Student deleted")
            found = True
            break

    if not found:
        print("Student not found")


def find_topper():
    if len(students) == 0:
        print("No students found")
        return

    max_marks = students[0][1]
    toppers = [students[0]]

    for s in students[1:]:
        if s[1] > max_marks:
            max_marks = s[1]
            toppers = [s]

        elif s[1] == max_marks:
            toppers.append(s)

    print("Topper(s):")
    for t in toppers:
        print(t[0], "| Marks:", t[1])


def search_student():
    srch = input("Enter student name: ")

    for s in students:
        if s[0].lower() == srch.lower():
            print("Found:", s[0], "| Marks:", s[1])
            break
    else:
        print("Not found")


# 🔥 MAIN LOOP (IMPORTANT FIX)
while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Find Topper")
    print("5. Search Student")
    print("6. Exit")

    oper = int(input("Enter operation: "))

    if oper == 1:
        AddStudent()

    elif oper == 2:
        ViewStudents()

    elif oper == 3:
        DeleteStudent()

    elif oper == 4:
        find_topper()

    elif oper == 5:
        search_student()

    elif oper == 6:
        print("Exiting...")
        break

    else:
        print("Invalid choice")