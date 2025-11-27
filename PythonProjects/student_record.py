import math

students = []
clubs = set()


def view_students():
    print("\n=== ALL STUDENTS ===")
    if not students:
        print("No student records available.")
        return

    for i, student in enumerate(students, start=1):
        print(
            f"{i}. Name: {student['name']}, Age: {student['age']}, Course: {student['course']}, Grades: {student['grades']}")


def add_student():
    print("\n=== ADD STUDENT ===")
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    print("Enter 3 grades:")
    try:
        g1 = float(input("Grade 1: "))
        g2 = float(input("Grade 2: "))
        g3 = float(input("Grade 3: "))
    except ValueError:
        print("Invalid grade entered.")
        return

    grades = (g1, g2, g3)

    student = {
        "name": name,
        "age": age,
        "course": course,
        "grades": grades
    }

    students.append(student)
    print("Student added.")


def manage_clubs():
    while True:
        print("\n=== CLUB MANAGEMENT ===")
        print("1. Add Club")
        print("2. View Clubs")
        print("3. Remove Club")
        print("4. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            club = input("Enter club name: ").strip()
            clubs.add(club)
            print("Club added.")
        elif choice == "2":
            print("\n=== REGISTERED CLUBS ===")
            if not clubs:
                print("No clubs available.")
            else:
                for c in clubs:
                    print(c)
        elif choice == "3":
            club = input("Enter club name to remove: ").strip()
            if club in clubs:
                clubs.remove(club)
                print("Club removed.")
            else:
                print("Club not found.")
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def show_grade_statistics():
    print("\n=== GRADE STATISTICS ===")

    if not students:
        print("No student data available.")
        return

    all_grades = []

    for student in students:
        all_grades.extend(list(student["grades"]))

    highest = max(all_grades)
    lowest = min(all_grades)
    average = math.floor(sum(all_grades) / len(all_grades))

    print(f"Highest Grade: {highest}")
    print(f"Lowest Grade: {lowest}")
    print(f"Average Grade (rounded down): {average}")


def main():
    while True:
        print("\n==== STUDENT RECORD ====")
        print("1. View All Students")
        print("2. Add Student")
        print("3. Manage Clubs")
        print("4. Show Grade Statistics")
        print("5. Exit")

        option = input("Select an option: ")

        if option == "1":
            view_students()
        elif option == "2":
            add_student()
        elif option == "3":
            manage_clubs()
        elif option == "4":
            show_grade_statistics()
        elif option == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
