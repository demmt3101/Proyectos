import pathlib
import typing
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QWidget
from PyQt5 import QtCore, QtGui, uic
from models.student_db import StudentDb
from controllers.student_form import StudentForm

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        mod_path = pathlib.Path(__file__).parent.parent
        uic.loadUi(mod_path / 'views/designer.ui', self)
        self._studentBD=StudentDb()
        self.load_students()
        self._studentForm = StudentForm()
        self.newStudentAction.triggered.connect(lambda: self._studentForm.show())
        self._studentForm.student_saved.connect(self.load_students)
        
        
    def load_students(self):
        student_list = self._studentBD.get_students()
        self.tableStudent.setRowCount(len(student_list))
        for i, student in enumerate(student_list):
            id, firts_name, last_name, email = student
            self.tableStudent.setItem(i, 0, QTableWidgetItem(str(id)))
            self.tableStudent.setItem(i, 1, QTableWidgetItem(str(firts_name)))
            self.tableStudent.setItem(i, 2, QTableWidgetItem(str(last_name)))
            self.tableStudent.setItem(i, 3, QTableWidgetItem(str(email)))
            
    def closeEvent(self, ev) -> None:
        self._studentBD.close()
        return super().closeEvent(ev)