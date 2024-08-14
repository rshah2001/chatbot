from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication
from PyQt6.QtCore import Qt, QMetaObject, Q_ARG
import sys
import threading
from backend import Chatbot


class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ai_chat = Chatbot()
        self.setMinimumSize(700, 500)


        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 680, 320)
        self.chat_area.setReadOnly(True)

        # Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 580, 40)

        # Add send button
        self.send_button = QPushButton("Send", self)
        self.send_button.setGeometry(600, 340, 80, 40)
        self.send_button.clicked.connect(self.send_message)
        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        if user_input:
            self.chat_area.append(f"<p style='color:#333333'>Me: {user_input}</p>")
            self.input_field.clear()

            thread = threading.Thread(target=self.get_bot_response, args=(user_input,))
            thread.start()

    def get_bot_response(self, user_input):
        response = self.ai_chat.get_response(user_input)
        QMetaObject.invokeMethod(self.chat_area, "append", Q_ARG(str, f"<p style='color:#333333; background-color:#E9E9E9'>Bot: {response}</p>"))


application = QApplication(sys.argv)
main_window = ChatBotWindow()
sys.exit(application.exec())
