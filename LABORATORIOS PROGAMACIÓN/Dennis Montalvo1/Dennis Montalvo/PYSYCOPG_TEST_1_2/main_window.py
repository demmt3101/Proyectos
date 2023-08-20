import typing
from PyQt5.QtWidgets import QMainWindow, QWidget, QTableWidgetItem
from PyQt5 import uic
from student_db import StudentDb

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self._student_db = StudentDb()
        uic.loadUi("main_window.ui", self)
        self.load_students()
        
    def load_students(self):
        student_list = self._student_db.get_students()
        self.studentsTable.setRowCount(len(student_list))
        for i, student in enumerate(student_list):
            id, first_name, last_name, email = student
            self.studentsTable.setItem(i, 0, QTableWidgetItem(str(id)))
            self.studentsTable.setItem(i, 1, QTableWidgetItem(first_name))
            self.studentsTable.setItem(i, 2, QTableWidgetItem(last_name))
            self.studentsTable.setItem(i, 3, QTableWidgetItem(email))