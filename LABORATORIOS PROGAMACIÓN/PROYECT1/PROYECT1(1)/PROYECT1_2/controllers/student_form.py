import pathlib 
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic

from models.students_db import StudentsDb

class StudentForm(QWidget):
    student_saved = pyqtSignal()
    def __init__(self):
        super().__init__()
        mod_path = pathlib.Path(__file__).parent.parent
        uic.loadUi(mod_path / "views/student_form.ui", self)
        self._students_db = StudentsDb()   
        self.bandera = True
        self.guardarButton.clicked.connect(self.save_student)
        self.cancelarButton.clicked.connect(lambda: self.close())
        
    def save_student(self):
        self.bandera = False
        self._students_db.create_student(
            self.nameText.text(), 
            self.lastnameText.text(),
            self.emailText.text()
        )
        self.student_saved.emit()
        self.close()
        self.nameText.setText("")
        self.lastnameText.setText("")
        self.emailText.setText("")
        self.bandera = True
        
        
        
    