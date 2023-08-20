import sys
from PyQt5 import QtWidgets
from calcu import Calcu

app = QtWidgets.QApplication(sys.argv)
first_sample_gui = Calcu()
first_sample_gui.show()
sys.exit(app.exec_())