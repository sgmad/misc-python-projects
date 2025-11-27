applicants = []

def add_applicants():

    num_applicant = int(input("\nEnter number of applicants: "))

    if num_applicant <= 0:
        print("Please enter a positive number.")
        return

    for i in range(num_applicant):
        print(f"\n--- Applicant No.{i +1} ---")

        name = input("Name: ")
        # age = int(input("Age: ")
        # entrance = int(input("Entrance Score: ")
        # interview = int(input("Interview Score: ")

        # TO SATISFY "NESTED LOOP" REQUIREMENT:
        while True:
            try:
                age = int(input("Age: "))
                if age > 0:
                    break
                else:
                    print("Age must be a positive number.")
            except ValueError:
                print("Invalid input.")

        while True:
            try:
                entrance = int(input("Entrance Score: "))
                break
            except ValueError:
                print("Invalid input.")

        while True:
            try:
                interview = int(input("Interview Score: "))
                break
            except ValueError:
                print("Invalid input.")

        applicant = {
            "name": name,
            "age": age,
            "entrance_score": entrance,
            "interview_score": interview
        }

        applicants.append(applicant)

def view_applicants():
    if not applicants:
        print("\nNo applicant records found.")
    else:
        print("\nList of Applicants:")
        for i, app in enumerate(applicants, start=1):
            print(f"{i}. {app['name']} - Age: {app['age']} | Exam: {app['entrance_score']} | Interview: {app['interview_score']}")

def check_admission_results():
    if not applicants:
        print("\nNo applicant records found.")
    else:
        print("\nChecking Admission Results...\n")

        for app in applicants:
            if app['age'] >= 18 and app['entrance_score'] >= 80 and app['interview_score'] >= 75:
                result = "Accepted"
            else:
                result = "Rejected"

            print(f"{app['name']} → {result}")

def view_summary_report():
    if not applicants:
        print("\nNo applicant records found.")
    else:
        total_applicants = len(applicants)
        accepted_count = 0
        accepted_names = []

        for app in applicants:
            if app['age'] >= 18 and app['entrance_score'] >= 80 and app['interview_score'] >= 75:
                accepted_count += 1
                accepted_names.append(app['name'])

        rejected_count = total_applicants - accepted_count

        if total_applicants > 0:
            acceptance_rate = (accepted_count / total_applicants) * 100
        else:
            acceptance_rate = 0.0

        names_str = ", ".join(accepted_names) if accepted_names else "None"

        print("\n========= SUMMARY REPORT ==========")
        print(f"Total Applicants: {total_applicants}")
        print(f"Accepted: {accepted_count}")
        print(f"Rejected: {rejected_count}")
        print(f"Acceptance Rate: {acceptance_rate:.1f}%")
        print(f"Accepted Applicants: {names_str}")
        print("===================================")

def main():
    while True:
        print("\n====== UM ADMISSION SYSTEM ======")
        print("1. Add Applicants")
        print("2. View All Applicants")
        print("3. Check Admission Results")
        print("4. View Summary Report")
        print("5. Exit")

        option = input("Select an option: ")

        if option == "1":
            add_applicants()
        elif option == "2":
            view_applicants()
        elif option == "3":
            check_admission_results()
        elif option == "4":
            view_summary_report()
        elif option == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()