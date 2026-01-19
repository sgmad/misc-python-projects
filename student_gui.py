# Name: Ugmad, Sam Christian M.
# Section: CS26L - 4381
# Date: 12/12/2025
# Description: User Interface for the Class List Manager.
# Contains layout logic, styling, and event handling.

from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, 
    QTextEdit, QVBoxLayout, QHBoxLayout, QFrame
)
from PyQt6.QtCore import Qt

# Import from other files
from student_model import Student
from student_manager import StudentManager

class StudentApp(QWidget):
    def __init__(self):
        super().__init__()
        self.manager = StudentManager()
        self.setWindowTitle("Class List Manager")

        # Full Screen Configuration
        self.showMaximized()

        # Dark Theme Style
        self.setStyleSheet("""
            QWidget {
                background-color: #1e2430;
                color: #e0e0e0;
                font-family: 'Segoe UI', sans-serif;
                font-size: 14px;
            }
            QLineEdit {
                background-color: #2b3442;
                border: 1px solid #3d4c63;
                color: #ffffff;
                padding: 8px;
                border-radius: 4px;
            }
            QTextEdit {
                background-color: #2b3442;
                border: 1px solid #3d4c63;
                color: #ffffff;
                padding: 5px;
            }
            QPushButton {
                background-color: #3b5c85;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #4a6fa5;
            }
            QLabel {
                color: #aebfd1;
                font-weight: bold;
            }
            /* Header Label Style */
            QLabel#Header {
                font-size: 20px;
                color: #ffffff;
                margin-bottom: 10px;
            }
        """)

        # Labels and Inputs
        self.lbl_header = QLabel("Class List Management")
        self.lbl_header.setObjectName("Header")
        self.lbl_header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.lbl_id = QLabel("Student ID:")
        self.txt_id = QLineEdit()

        self.lbl_name = QLabel("Name:")
        self.txt_name = QLineEdit()

        self.lbl_course = QLabel("Course / Section:")
        self.txt_course = QLineEdit()

        # Buttons
        self.btn_add = QPushButton("Add Student")
        self.btn_load = QPushButton("Load Students")

        # Display Area
        self.display = QTextEdit()
        self.display.setReadOnly(True)

        # Layout Management
        
        # Form Layout (Vertical)
        form_layout = QVBoxLayout()
        form_layout.addWidget(self.lbl_header)
        form_layout.addWidget(self.lbl_id)
        form_layout.addWidget(self.txt_id)
        form_layout.addWidget(self.lbl_name)
        form_layout.addWidget(self.txt_name)
        form_layout.addWidget(self.lbl_course)
        form_layout.addWidget(self.txt_course)
        form_layout.addSpacing(15)
        form_layout.addWidget(self.btn_add)
        form_layout.addWidget(self.btn_load)
        form_layout.addSpacing(15)
        form_layout.addWidget(self.display)

        # Container Widget (Fixed width to center form)
        self.container = QFrame()
        self.container.setLayout(form_layout)
        self.container.setFixedWidth(600)
        
        # Horizontal Centering
        center_layout = QHBoxLayout()
        center_layout.addStretch()
        center_layout.addWidget(self.container)
        center_layout.addStretch()

        # Vertical Centering
        main_layout = QVBoxLayout()
        main_layout.addStretch()
        main_layout.addLayout(center_layout)
        main_layout.addStretch()

        self.setLayout(main_layout)

        # Signals
        self.btn_add.clicked.connect(self.add_student)
        self.btn_load.clicked.connect(self.load_students)

    def add_student(self):
        student = Student(
            self.txt_id.text(),
            self.txt_name.text(),
            self.txt_course.text()
        )

        if student.student_id and student.name and student.course:
            self.manager.save_student(student)

            # Clear inputs after saving
            self.txt_id.clear()
            self.txt_name.clear()
            self.txt_course.clear()
        else:
            self.display.setText("Error: Please fill in all fields.")

    def load_students(self):
        self.display.clear()
        students = self.manager.load_students()
        
        if not students:
            self.display.setText("No records found.")
            return

        # Build HTML Table for output
        html = """
        <table border='1' cellspacing='0' cellpadding='5' width='100%' style='border-color: #3d4c63;'>
            <tr>
                <th style='background-color: #2b3442; color: #ffffff;'>Student ID</th>
                <th style='background-color: #2b3442; color: #ffffff;'>Name</th>
                <th style='background-color: #2b3442; color: #ffffff;'>Course / Section</th>
            </tr>
        """
        
        for student_str in students:
            parts = student_str.split(',')
            if len(parts) == 3:
                html += f"""
                <tr>
                    <td>{parts[0]}</td>
                    <td>{parts[1]}</td>
                    <td>{parts[2]}</td>
                </tr>
                """
            else:
                html += f"<tr><td colspan='3'>{student_str}</td></tr>"
        
        html += "</table>"
        self.display.setHtml(html)