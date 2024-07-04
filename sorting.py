#sort() method = used in lists
#sort() function = used in iterables

"""
students = ["kilonzo","Amos","terence","prezoo","mkurugezii"]
#students.sort(reverse=True)
sorted_students = sorted(students,reverse=True)

for i in sorted_students:
    print(i)
"""

students = [("Kilonzo","A",87),
            ("Prezoo","B",65),
            ("Terence","C",53),
            ("mkuru","B",69)]

grade = lambda grades:grades[1]
#students.sort(key=grade)
sorted_students = sorted(students,key=grade)

for i in sorted_students:
    print(i)