# Name: Ugmad, Sam Christian M.
# Section: CS26L - 4381
# Date: 12/12/2025
# Description: Handles file operations for student records.

class StudentManager:
    def __init__(self, filename="students.txt"):
        self.filename = filename

    def save_student(self, student):
        # Uses print() to automatically handle line breaks
        try:
            with open(self.filename, "a") as file:
                print(student.to_string(), file=file)
        except IOError as e:
            print(f"Error saving student: {e}")

    def load_students(self):
        try:
            with open(self.filename, "r") as file:
                return file.read().splitlines()
        except FileNotFoundError:
            return []