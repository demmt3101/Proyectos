from PyQt5 import QtWidgets, QtCore

class Calcu(QtWidgets.QWidget):
    def __init__(self) -> None:
        super(). __init__()
        
        self._v_layout = QtWidgets.QVBoxLayout()
        self._result_text = QtWidgets.QLineEdit("0")
        self._reset_assign = False
        self.initUI()
        
    def initUI(self):
        grid_layout = QtWidgets.QGridLayout()
        self.setLayout(self._v_layout)
        self._v_layout.addWidget(self._result_text)
        self._v_layout.addLayout(grid_layout)
        self.setWindowTitle("Calculadora")
        self.setMinimumSize(200, 400)
        self._result_text.setAlignment(QtCore.Qt.AlignRight)
        
        #boton 7
        button_7 = QtWidgets.QPushButton("7")
        grid_layout.addWidget(button_7, 0, 0)
        button_7.clicked.connect(lambda: self.number_click("7"))
        
        #boton 8
        button_8 = QtWidgets.QPushButton("8")
        grid_layout.addWidget(button_8, 0, 1)
        button_8.clicked.connect(lambda: self.number_click("8"))
        
        #boton 9
        button_9 = QtWidgets.QPushButton("9")
        grid_layout.addWidget(button_9, 0, 2)
        button_9.clicked.connect(lambda: self.number_click("9"))
        
        #boton suma
        button_addition = QtWidgets.QPushButton("+")
        grid_layout.addWidget(button_addition, 0, 3)
        button_addition.setStyleSheet("QPushButton {background-color: #334fff}")
        button_addition.clicked.connect(lambda: self.init_calc('+'))
        
        #boton 4
        button_4 = QtWidgets.QPushButton("4")
        grid_layout.addWidget(button_4, 1, 0)
        button_4.clicked.connect(lambda: self.number_click("4"))
        
        #boton 5
        button_5 = QtWidgets.QPushButton("5")
        grid_layout.addWidget(button_5, 1, 1)
        button_5.clicked.connect(lambda: self.number_click("5"))
        
        #boton 6
        button_6 = QtWidgets.QPushButton("6")
        grid_layout.addWidget(button_6, 1, 2)
        button_6.clicked.connect(lambda: self.number_click("6"))
        
        #boton resta
        button_subtraction = QtWidgets.QPushButton("-")
        grid_layout.addWidget(button_subtraction, 1, 3)
        button_subtraction.setStyleSheet("QPushButton {background-color: #334fff}")
        button_subtraction.clicked.connect(lambda: self.init_calc('-'))
        
        #boton 1
        button_1 = QtWidgets.QPushButton("1")
        grid_layout.addWidget(button_1, 2, 0)
        button_1.clicked.connect(lambda: self.number_click("1"))
        
        #boton 2
        button_2 = QtWidgets.QPushButton("2")
        grid_layout.addWidget(button_2, 2, 1)
        button_2.clicked.connect(lambda: self.number_click("2"))
        
        #boton 3
        button_3 = QtWidgets.QPushButton("3")
        grid_layout.addWidget(button_3, 2, 2)
        button_3.clicked.connect(lambda: self.number_click("3"))
        
        #boton división
        button_division = QtWidgets.QPushButton("/")
        grid_layout.addWidget(button_division, 2, 3)
        button_division.setStyleSheet("QPushButton {background-color: #334fff}")
        button_division.clicked.connect(lambda: self.init_calc('/'))

        #boton 0
        button_0 = QtWidgets.QPushButton("0")
        grid_layout.addWidget(button_0, 3, 0)
        button_0.clicked.connect(lambda: self.number_click("0"))
        
        #boton punto
        button_point = QtWidgets.QPushButton(".")
        grid_layout.addWidget(button_point, 3, 1)
        button_point.clicked.connect(lambda: self.number_click("."))
        
        #boton igual
        button_assign = QtWidgets.QPushButton("=")
        grid_layout.addWidget(button_assign, 3, 2)
        button_assign.setStyleSheet("QPushButton {background-color: #334fff}")
        button_assign.clicked.connect(lambda: self.calculate())
        
        #boton multiplicación
        button_multiplication = QtWidgets.QPushButton("x")
        grid_layout.addWidget(button_multiplication, 3, 3)
        button_multiplication.setStyleSheet("QPushButton {background-color: #334fff}")
        button_multiplication.clicked.connect(lambda: self.init_calc('x'))

        #boton borrar
        button_delete = QtWidgets.QPushButton("C")
        grid_layout.addWidget(button_delete, 4, 0, 1, 2)
        button_delete.setStyleSheet("QPushButton {background-color: #334fff}")
        button_delete.clicked.connect(lambda: self._result_text.setText("0"))
        
        #boton reseteo
        button_reset = QtWidgets.QPushButton("AC")
        grid_layout.addWidget(button_reset, 4, 2, 1, 2)
        button_reset.setStyleSheet("QPushButton {background-color: #FF3333}")
        button_reset.clicked.connect(lambda: self.clear_all())
        
    def number_click(self, txt: str):
        #print("El boton fue aplastado", txt)
        result_str = self._result_text.text()
        if txt == '.' and ('.' in result_str):
            return
        if result_str == '0'or result_str == '0.0' or self._reset_assign:
            self._result_text.setText(txt)
        else:
            self._result_text.setText(result_str +txt)

    def init_calc(self, operator: str):
        self._mem = float(self._result_text.text())
        self._operator = operator
        self._result_text.setText("0")

    def calculate(self):
        match self._operator:
            case '+':
                self._mem += float(self._result_text.text())
            case '-':
                self._mem -= float(self._result_text.text())
            case 'x':
                self._mem *= float(self._result_text.text())
            case '/':
                self._mem /= float(self._result_text.text())
            case other:
                self._mem = float(self._result_text.text())

        self._result_text.setText(str(self._mem))
        self._reset_assign = False
        self._operator = ''
    def clear_all(self):
         self._result_text.setText('0')
         self._mem = 0.0
         self._operator = '0.0'
