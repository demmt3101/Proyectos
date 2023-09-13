from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Eliminar fila con botón")

        # Crear la tabla
        self.table_widget = QTableWidget()
        self.setCentralWidget(self.table_widget)

        # Agregar datos de ejemplo a la tabla
        self.table_widget.setColumnCount(4)
        self.table_widget.setRowCount(3)
        self.table_widget.setHorizontalHeaderLabels(["ID", "Nombre", "Apellido", ""])

        self.table_widget.setItem(0, 0, QTableWidgetItem("1"))
        self.table_widget.setItem(0, 1, QTableWidgetItem("John"))
        self.table_widget.setItem(0, 2, QTableWidgetItem("Doe"))

        self.table_widget.setItem(1, 0, QTableWidgetItem("2"))
        self.table_widget.setItem(1, 1, QTableWidgetItem("Jane"))
        self.table_widget.setItem(1, 2, QTableWidgetItem("Smith"))

        self.table_widget.setItem(2, 0, QTableWidgetItem("3"))
        self.table_widget.setItem(2, 1, QTableWidgetItem("Alice"))
        self.table_widget.setItem(2, 2, QTableWidgetItem("Johnson"))

        # Agregar botón de eliminar en cada fila
        for row in range(self.table_widget.rowCount()):
            btn_eliminar = QPushButton("Eliminar")
            btn_eliminar.clicked.connect(lambda _, r=row: self.eliminar_fila(r))
            self.table_widget.setCellWidget(row, 3, btn_eliminar)

        # Diseño de la interfaz
        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def eliminar_fila(self, row):
        self.table_widget.removeRow(row)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
