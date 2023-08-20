import sys
from PyQt5.QtWidgets import QApplication
from controllers.main_window import MainWindow

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
sys.exit(app.exec_())