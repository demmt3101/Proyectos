import pathlib as path
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QPushButton
from PyQt5 import QtCore, uic, QtWidgets

from models.students_db import StudentsDb
from controllers.student_form import StudentForm

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        mod_path = path.Path(__file__).parent.parent
        uic.loadUi(mod_path / "views/main_window.ui", self)
        self._students_db = StudentsDb()
        self._student_form = StudentForm()
        self.newStudentAction.triggered.connect(lambda: self._student_form.show())  
        self._student_form.student_saved.connect(self.loadStudents)
        self.exitAction.triggered.connect(lambda: self.close())      
        self.bandera = False
        self.loadStudents()
        
    def loadStudents(self):
        student_list = self._students_db.get_students()
        self.studentsTable.setRowCount(len(student_list))
        self.studentsTable.setColumnCount(5)
        for i, student in enumerate(student_list):
            id, first_name, last_name, email = student
            deleteButton = QPushButton("Delete")
            self.studentsTable.setItem(i,0,QTableWidgetItem(str(id)))
            self.studentsTable.setItem(i,1,QTableWidgetItem(str(first_name)))
            self.studentsTable.setItem(i,2,QTableWidgetItem(str(last_name)))
            self.studentsTable.setItem(i,3,QTableWidgetItem(str(email)))
            self.studentsTable.setCellWidget(i,4, deleteButton)
            self.studentsTable.setColumnWidth(4, 100)
            self.studentsTable.item(i,0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            deleteButton.clicked.connect(self.deleteList)
        
        self.studentsTable.itemChanged.connect(self.onItemChanged)  
            
    def onItemChanged(self, item):
        if self._student_form.bandera:
            rowValues = []
            for column in range(self.studentsTable.columnCount()-1):
                rowValues.append(self.studentsTable.item(item.row(), column).text()) 
                
            if self._students_db.update_student(rowValues[0],
                                                rowValues[1],
                                                rowValues[2],
                                                rowValues[3]
                                                ): 
                
                msg = "El estudiante fue guardado exitosamente"
            else:
                msg = "Hubo un problema al guardar el estudiante. Vuelva a intentar."
                
            if self.bandera:
                QMessageBox.information(self, "Mensaje emergente", msg, QMessageBox.Ok)   
            
    
    def deleteList(self):
        button = self.sender()
        row = self.studentsTable.indexAt(button.pos()).row()
        msgBox = QMessageBox.question(self, "Confirmacion", "El usuario sera eliminado. ¿Quiere continuar?", QMessageBox.Yes | QMessageBox.No)
        if QMessageBox.Yes:
            self.studentsTable.removeRow(row)
            self._students_db.delete_student(self.studentsTable.item(row, 0).text())
            QMessageBox.information(self, "Eliminacion Exitosa", "La eliminacion del estudiante fue exitosa")
        else:
            QMessageBox.critical(self, "ERROR", "Hubo un problema al eliminar el estudiante")
    
    def closeEvent(self, ev) -> None:
        self._students_db.close()
        return super().closeEvent(ev)
            
          
        
        
        
            
    
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
