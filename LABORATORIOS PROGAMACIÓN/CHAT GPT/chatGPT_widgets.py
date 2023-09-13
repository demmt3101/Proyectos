import typing
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from Chat_GPT import ChatGPTHandler

class GptWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('chat.ui', self)
        self.SendTextButton.clicked.connect(lambda: self.response())

        
    def onButtonClicked(self):
        chatText = self.lineEdit.text()
        self.textEdit.append("Tú: " + chatText)
        
    def response(self):
        chatHistory = self.lineEdit.text()
        chatResponse = ChatGPTHandler.askChatGPT(self, chatHistory)
        self.textEdit.append("Tú: " + chatHistory)
        self.textEdit.append("ChatGPT:"+ chatResponse)
        
    def keyPressEvent(self, qKeyEvent):
        if qKeyEvent.key() == QtCore.Qt.Key_Return:
            self.response()
        else:
            super().keyPressEvent(qKeyEvent)
        