# sort() method   = used with lists
# sort() function = used with iterables

# list
# fruits = ["banana", "apple", "papaya", "mango"]
# fruits.sort()
#
# for i in fruits:
#     print(i)

# tuple
# fruits = ("banana", "apple", "papaya", "mango")
# fruit = sorted(fruits)
#
# for i in fruit:
#     print(i)

# list of tuple


# students = [("Squidward", "F", 60),
#             ("Sandy", "A", 33),
#             ("Patrick", "D", 36),
#             ("Spongebob", "B", 20),
#             ("Mr.Krabs", "C", 78)]


students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78))

# sort by name
# students.sort()
# for i in students:
#     print(i)

# sort by key value
grade = lambda grades: grades[1]

age = lambda ages: ages[2]

sorted_student = sorted(students, key=grade)
sorted_student_age = sorted(students, key=age)

# students.sort(key=age)

for i in sorted_student:
    print(i)
