import sys
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow

app = QApplication(sys.argv)
MainWindow = MainWindow()
MainWindow.show()
sys.exit(app.exec_())