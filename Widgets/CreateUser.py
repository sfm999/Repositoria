from resources.qt_resources.qt_widgets import *
from Widgets.LineEditCombo import LineEditCombo


class CreateUser(QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout(QGridLayout())

        self.username_area = LineEditCombo('Username: ')
        self.layout().addWidget(self.username_area, 1, 0)

        self.password_area = LineEditCombo('Password: ')
        self.layout().addWidget(self.password_area, 2, 0)

        self.email_area = LineEditCombo('Email: ')
        self.layout().addWidget(self.email_area, 3, 0)

        self.create_btn = QPushButton('Create User')
        self.create_btn.clicked.connect(self.btn_pressed)
        self.layout().addWidget(self.create_btn, 4, 0)
        self.show()

    def get_usn_text(self):
        return self.username_area.get_text()

    def get_pwd_text(self):
        return self.password_area.get_text()

    def get_email_text(self):
        return self.email_area.get_text()

    def btn_pressed(self):
        print('hello')