import typing
import pathlib
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5 import QtGui, uic, QtCore
from controllers.student_form import StudentForm
from models.students_db import StudentDB

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        mod_path = pathlib.Path(__file__).parent.parent
        uic.loadUi(mod_path / "views/main_window.ui", self)
        self._student_db = StudentDB()
        self.load_students()
        self._studentForm = StudentForm()
        self.newStudentAction.triggered.connect(lambda: self._studentForm.show())
        self._studentForm.student_saved.connect(self.load_students)

    def load_students(self):
        student_list = self._student_db.get_students()
        self.studentsTable.setRowCount(len(student_list))
        self.studentsTable.item(i,0).setFlags(QtCore.Qt.ItemEnabled | QtCore.Qt.ItemIsSelectable)
        for i, student in enumerate(student_list):
            id, first_name, last_name, email = student
            self.studentsTable.setItem(i, 0, QTableWidgetItem(str(id)))
            self.studentsTable.setItem(i, 1, QTableWidgetItem(first_name))
            self.studentsTable.setItem(i, 2, QTableWidgetItem(last_name))
            self.studentsTable.setItem(i, 3, QTableWidgetItem(email))
    
    def onItemChanged(self, item):
        rowValues = []
        for column in range(self.studentsTable.columnCount()):
            rowValues.append(self.studentsTable.item(item.row(), column).text())

    def closeEvent(self, ev) -> None:
        self._student_db.close()
        return super().closeEvent(ev)