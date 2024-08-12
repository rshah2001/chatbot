from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication
import sys

class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 500)

        #  Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)
        # add the input field Widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)
        # add send button
        self.send_button = QPushButton("Send", self)
        self.send_button.setGeometry(500, 345, 100, 40)

        self.show()

class Chatbot:
    pass



application = QApplication(sys.argv)
main_window = ChatBotWindow()
sys.exit(application.exec())
