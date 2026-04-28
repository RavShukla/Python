# d1 = {}
# d2 = {}
#
# # First dictionary (roll_no → name)
# while True:
#     roll_no = input("Enter student ROLL NO: ")
#     name = input("Enter student name: ")
#
#     d1[roll_no] = name
#
#     choice = input("Add another student? (y/n): ")
#     if choice.lower() == "n":
#         break
#
#
# # Second dictionary (roll_no → marks)
# while True:
#     roll_no = input("Enter student ROLL NO: ")
#     marks = int(input("Enter student marks: "))
#
#     d2[roll_no] = marks
#
#     choice = input("Add another student? (y/n): ")
#     if choice.lower() == "n":
#         break
#
#
# # 🔥 Merge properly
# d3 = {}
#
# for roll_no in d1:
#     d3[roll_no] = {
#         "name": d1[roll_no],
#         "marks": d2.get(roll_no, None)  # safe access
#     }
#
# print("\nFinal Student Data:")
# print(d3)



d1 = {"Gaurav":20 , "Gurmeet":19}
d2 = {"Devansh":19 , "Harshit":19}
d3 = d1 | d2
print(d3)
