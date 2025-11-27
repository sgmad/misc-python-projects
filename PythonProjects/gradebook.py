
students = {
    "Sam": 85,
    "Steven": 92,
    "Jonathan": 78,
    "James": 90,
    "Kyle": 88,
}

def display_gradebook(d):
    print("\nStudent Gradebook:")
    for name, grade in d.items():
        print(f"{name} -> {grade}")
    print()

# Display gradebook
display_gradebook(students)

# Search name
search_name = "Jonathan"
print(f"Search for student: {search_name}")
if search_name in students:
    print(f"{search_name}'s grade is: {students[search_name]}")
else:
    print("Student not found.")
print()

# Update grade
update_name = "Jonathan"
new_grade = 82
if update_name in students:
    old_grade = students[update_name]
    print(f"Updating grade: {update_name} -> {old_grade} to {new_grade}")
    students[update_name] = new_grade
else:
    print("Student not found.")
print()

# Display updated gradebook
print("Updated Gradebook:")
display_gradebook(students)

# Find top student WITHOUT using max()
top_student = None
top_grade = -1
for name, grade in students.items():
    if grade > top_grade:
        top_student = name
        top_grade = grade

if top_student is not None:
    print(f"Top student: {top_student} with grade {top_grade}")
else:
    print("No students in gradebook.")
