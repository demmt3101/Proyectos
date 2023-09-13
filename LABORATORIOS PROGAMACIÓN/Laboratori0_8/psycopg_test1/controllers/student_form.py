import pathlib
import typing
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore, uic
from models.student_db import StudentDb

class StudentForm(QWidget):
    student_saved = pyqtSignal()
    def __init__(self) -> None:
        super().__init__()
        self.__studentHandler = StudentDb()
        mod_path = pathlib.Path(__file__).parent.parent
        uic.loadUi(mod_path / 'views/student_form.ui',self)
        self.saveButton.clicked.connect(lambda: self.save_student())
        self.cancelButton.clicked.connect(lambda: self.close())
        
    def save_student(self):
        self.__studentHandler.create_students(self.firstNameTextField.text(),self.lastNameTextField.text(), self.emailTextField.text())
        self.student_saved.emit()
        self.close()
        