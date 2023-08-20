import sys
from PyQt5.QtWidgets import QApplication
from chatGPT_widgets import GptWidget
from Chat_GPT import ChatGPTHandler

app = QApplication(sys.argv)
gptWidget = GptWidget()
gptWidget.show()
sys.exit(app.exec_())