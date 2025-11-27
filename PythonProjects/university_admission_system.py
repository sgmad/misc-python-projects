applicants = []


def add_applicants():

    try:
        # Ask how many applicants to add
        num_to_add = int(input("\nEnter number of applicants: "))

        if num_to_add <= 0:
            print("Please enter a positive number.")
            return  # Stop the function and return to menu

        # Loop for each new applicant
        for i in range(num_to_add):
            print(f"\n--- Applicant No.{i + 1} ---")
            name = input("Name: ")

            # --- Nested loops for input validation ---
            while True:
                try:
                    age = int(input("Age: "))
                    if age > 0:
                        break  # Exit validation loop
                    else:
                        print("Age must be a positive number.")
                except ValueError:
                    print("Invalid input. Please enter a whole number for age.")

            while True:
                try:
                    exam_score = int(input("Entrance Score: "))
                    break  # Exit validation loop
                except ValueError:
                    print("Invalid input. Please enter a whole number for the score.")

            while True:
                try:
                    interview_score = int(input("Interview Score: "))
                    break  # Exit validation loop
                except ValueError:
                    print("Invalid input. Please enter a whole number for the score.")

            # Store data in a dictionary
            applicant_data = {
                "name": name,
                "age": age,
                "exam_score": exam_score,
                "interview_score": interview_score
            }

            # Add the new applicant dictionary to the main list
            applicants.append(applicant_data)

        print(f"\nSuccessfully added {num_to_add} applicant(s).")

    except ValueError:
        print("Invalid input. Please enter a whole number for the number of applicants.")


def view_applicants():
    """Displays all applicants currently in the system."""
    if not applicants:  # Check if the list is empty
        print("\nNo applicant records found.")
    else:
        print("\nList of Applicants:")
        # Use enumerate to get a number for each applicant (starting from 1)
        for i, app in enumerate(applicants, start=1):
            print(
                f"{i}. {app['name']} - Age: {app['age']} | Exam: {app['exam_score']} | Interview: {app['interview_score']}")


def check_admission_results():
    """Checks and displays the admission status for each applicant."""
    if not applicants:
        print("\nNo applicant records found.")
    else:
        print("\nChecking Admission Results...")
        # Loop through each applicant and check their status
        for app in applicants:
            # Apply nested conditions
            if app['age'] >= 18 and app['exam_score'] >= 80 and app['interview_score'] >= 75:
                result = "Accepted"
            else:
                result = "Rejected"

            print(f"{app['name']} → {result}")


def view_summary_report():
    """Displays a summary of all applicants and admission statistics."""
    if not applicants:
        print("\nNo applicant records found.")
    else:
        total_applicants = len(applicants)
        accepted_count = 0
        accepted_names = []

        # Re-run the logic to gather stats
        for app in applicants:
            if app['age'] >= 18 and app['exam_score'] >= 80 and app['interview_score'] >= 75:
                accepted_count += 1
                accepted_names.append(app['name'])

        rejected_count = total_applicants - accepted_count

        # Calculate acceptance rate, handling division by zero
        if total_applicants > 0:
            acceptance_rate = (accepted_count / total_applicants) * 100
        else:
            acceptance_rate = 0.0

        # Format the list of accepted names for printing
        names_str = ", ".join(accepted_names) if accepted_names else "None"

        # Print the report
        print("\n========= SUMMARY REPORT ==========")
        print(f"Total Applicants: {total_applicants}")
        print(f"Accepted: {accepted_count}")
        print(f"Rejected: {rejected_count}")
        print(f"Acceptance Rate: {acceptance_rate:.1f}%")
        print(f"Accepted Applicants: {names_str}")
        print("===================================")


def main():
    """Main function to run the menu-driven system."""
    while True:
        # --- MAIN MENU ---
        print("\n====== UM ADMISSION SYSTEM ======")
        print("1. Add Applicants")
        print("2. View All Applicants")
        print("3. Check Admission Results")
        print("4. View Summary Report")
        print("5. Exit")

        option = input("      Enter your choice (1-5): ")

        if option == '1':
            add_applicants()
        elif option == '2':
            view_applicants()
        elif option == '3':
            check_admission_results()
        elif option == '4':
            view_summary_report()
        elif option == '5':
            print("\nThank you for using the UM Admission System. Goodbye!")
            break  # Exit the main 'while True' loop
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")


# This line ensures that main() only runs when the script is executed directly
if __name__ == "__main__":
    main()

# Save this file as: Lastname_admission.py

# This list will store all applicant data.
# Each applicant will be a dictionary.
applicants = []

while True:
    # --- MAIN MENU ---
    print("\n====== UM ADMISSION SYSTEM ======")
    print("1. Add Applicants")
    print("2. View All Applicants")
    print("3. Check Admission Results")
    print("4. View Summary Report")
    print("5. Exit")

    choice = input("      Enter your choice (1-5): ")

    # --- 1. Add Applicants ---
    if choice == '1':
        try:
            # Ask how many applicants to add
            num_to_add = int(input("Enter number of applicants: "))

            if num_to_add <= 0:
                print("Please enter a positive number.")
                continue  # Go back to the main menu

            # Loop for each new applicant
            for i in range(num_to_add):
                print(f"\n--- Applicant No.{i + 1} ---")
                name = input("Name: ")

                # Nested loop for Age validation
                while True:
                    try:
                        age = int(input("Age: "))
                        if age > 0:
                            break  # Exit validation loop
                        else:
                            print("Age must be a positive number.")
                    except ValueError:
                        print("Invalid input. Please enter a whole number for age.")

                # Nested loop for Entrance Score validation
                while True:
                    try:
                        exam_score = int(input("Entrance Score: "))
                        break  # Exit validation loop
                    except ValueError:
                        print("Invalid input. Please enter a whole number for the score.")

                # Nested loop for Interview Score validation
                while True:
                    try:
                        interview_score = int(input("Interview Score: "))
                        break  # Exit validation loop
                    except ValueError:
                        print("Invalid input. Please enter a whole number for the score.")

                # Store data in a dictionary
                applicant_data = {
                    "name": name,
                    "age": age,
                    "exam_score": exam_score,
                    "interview_score": interview_score
                }

                # Add the new applicant dictionary to the main list
                applicants.append(applicant_data)

            print(f"\nSuccessfully added {num_to_add} applicant(s).")

        except ValueError:
            print("Invalid input. Please enter a whole number for the number of applicants.")

    # --- 2. View All Applicants ---
    elif choice == '2':
        if not applicants:  # Check if the list is empty
            print("\nNo applicant records found.")
        else:
            print("\nList of Applicants:")
            # Use enumerate to get a number for each applicant (starting from 1)
            for i, app in enumerate(applicants, start=1):
                print(
                    f"{i}. {app['name']} - Age: {app['age']} | Exam: {app['exam_score']} | Interview: {app['interview_score']}")

    # --- 3. Check Admission Results ---
    elif choice == '3':
        if not applicants:
            print("\nNo applicant records found.")
        else:
            print("\nChecking Admission Results...")
            # Loop through each applicant and check their status
            for app in applicants:
                # Apply nested conditions
                if app['age'] >= 18 and app['exam_score'] >= 80 and app['interview_score'] >= 75:
                    result = "Accepted"
                else:
                    result = "Rejected"

                print(f"{app['name']} → {result}")

    # --- 4. View Summary Report ---
    elif choice == '4':
        if not applicants:
            print("\nNo applicant records found.")
        else:
            total_applicants = len(applicants)
            accepted_count = 0
            accepted_names = []

            # Re-run the logic to gather stats
            for app in applicants:
                if app['age'] >= 18 and app['exam_score'] >= 80 and app['interview_score'] >= 75:
                    accepted_count += 1
                    accepted_names.append(app['name'])

            rejected_count = total_applicants - accepted_count

            # Calculate acceptance rate, handling division by zero
            if total_applicants > 0:
                acceptance_rate = (accepted_count / total_applicants) * 100
            else:
                acceptance_rate = 0.0

            # Format the list of accepted names for printing
            if not accepted_names:
                names_str = "None"
            else:
                names_str = ", ".join(accepted_names)

            # Print the report
            print("\n========= SUMMARY REPORT ==========")
            print(f"Total Applicants: {total_applicants}")
            print(f"Accepted: {accepted_count}")
            print(f"Rejected: {rejected_count}")
            print(f"Acceptance Rate: {acceptance_rate:.1f}%")
            print(f"Accepted Applicants: {names_str}")
            print("===================================")

    # --- 5. Exit ---
    elif choice == '5':
        print("\nThank you for using the UM Admission System. Goodbye!")
        break  # Exit the main 'while True' loop

    # --- Invalid Choice ---
    else:
        print("\nInvalid choice. Please enter a number between 1 and 5.")
