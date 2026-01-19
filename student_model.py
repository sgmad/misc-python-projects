# Name: Ugmad, Sam Christian M.
# Section: CS26L - 4381
# Date: 12/12/2025
# Description: Defines the Student data model.

class Student:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def to_string(self):
        return f"{self.student_id},{self.name},{self.course}"