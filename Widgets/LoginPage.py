from resources.qt_resources.qt_widgets import *
from resources.qt_resources.qt_core import *
from Widgets.LineEditCombo import LineEditCombo
from db.controller.db import DB

"""
    TODO:
        - Add login button
        - Add background widget to base
            - Move child_one to background widget
            - Implement background image on background widget
"""


class LoginSetup(QWidget):
    def setup_ui(self, LoginPage):

        # Set size and object name for LoginPage widget
        LoginPage.setObjectName('Repositoria | User Login')
        LoginPage.resize(651, 451)

        # Create background widget
        self.background_widget = QWidget(LoginPage)
        self.background_widget.setObjectName('CentralWidget')

        # Create background layout
        self.h_layout = QHBoxLayout(self.background_widget)

        # Set background layout spacing, etc.
        self.h_layout.setContentsMargins(11, 11, 11, 11)
        self.h_layout.setSpacing(6)
        self.h_layout.setObjectName("HorizontalLayout2")


        # Create fore widget with background as parent and set its layout
        self.fore_widget = QWidget(self.background_widget)
        self.fore_widget.setLayout(QVBoxLayout())
        self.fore_widget.setObjectName('ForeWidget')

        # Set fore widget sizing
        self.fore_widget.layout().setContentsMargins(60, 60, 60, 60)
        self.fore_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.fore_widget.setMaximumSize(700, 620)

        # Set fore layout spacing, etc.
        self.fore_widget.layout().setSpacing(6)

        # Set up the login functionality widgets
        self.username_widget = LineEditCombo('Username: ')
        self.username_widget.inp.setPlaceholderText('Username')

        # Password widget
        self.password_widget = LineEditCombo('Password: ')
        self.password_widget.inp.setPlaceholderText('Password')
        self.password_widget.inp.setEchoMode(QLineEdit.Password)

        # Login button
        self.login_button = QPushButton('Login', self.background_widget)

        # Add the widgets to Horizontal Layout 1
        self.fore_widget.layout().addWidget(self.username_widget)
        self.fore_widget.layout().addWidget(self.password_widget)
        self.fore_widget.layout().addWidget(self.login_button)

        # Add Horizontal Layout 1 to Horizontal Layout 2 (put login on background widget)
        self.h_layout.addWidget(self.fore_widget)

        # Set the LoginPage central widget as background widget
        LoginPage.setCentralWidget(self.background_widget)

        # Create menu bar
        self.menu_bar = QMenuBar(LoginPage)
        self.menu_bar.setObjectName('MenuBar')

        # Set menu bar spacing, etc.
        self.menu_bar.setGeometry(0, 0, 651, 26)
        self.show()

    def login_clicked(self):
        self.db = DB()
        res = self.db.execute_read_query("SELECT username FROM users WHERE username = '%s';"
                                         % self.username_widget.get_text())
        print(res)
        if not res:
            print('test')


class LoginPage(QMainWindow, LoginSetup):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(stylesheet)
        # Init the LoginPage framework
        self.setup_ui(self)


stylesheet = """
    LoginPage {
        background-image: url("resources/images/books2.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""