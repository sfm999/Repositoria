from Widgets.LineEditCombo import LineEditCombo
from Widgets.CreateUser import CreateUser
from Widgets.LoginPage import LoginPage
from resources.qt_resources.qt_widgets import *
from resources.qt_resources.qt_core import *
from db.controller.db import DB


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Init the db class object variable
        self.db = None

        # Add a title
        self.setWindowTitle("Everyday GUI")

        # Set up gui exit button clicked
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        # Main layout and
        self.stack = QStackedLayout()

        # Create login-page (page 0 of stack)
        self.login_page = LoginPage()
        self.create_user_page = CreateUser()
        self.stack.insertWidget(1, self.create_user_page)

        # Add the login_page to the stack
        self.stack.insertWidget(0, self.login_page)
        # Set the main layout as the stacked layout
        self.setLayout(self.stack)
        # Add the login_page widget to the stack
        self.stack.setCurrentIndex(0)

        # Set up the main page that login leads to
        self.main_page = QWidget()

        # Set main_page layout
        self.main_page.setLayout(QHBoxLayout())

        # Create the widget for left hand side of main_page
        self.lhs_bar = QWidget()
        self.lhs_bar.setLayout(QHBoxLayout())
        # Add the lhs_bar to the main_page
        self.main_page.layout().addWidget(self.lhs_bar)

        # Add a test widget to see it made it there
        self.lhs_bar.layout().addWidget(LineEditCombo('TEST'))

        self.mid_bar = QWidget()
        self.mid_bar.setLayout(QHBoxLayout())
        self.mid_bar.layout().addWidget(LineEditCombo('TEST'))
        self.main_page.layout().addWidget(self.mid_bar)

        self.rhs_bar = QWidget()
        self.rhs_bar.setLayout(QHBoxLayout())
        self.rhs_bar.layout().addWidget(LineEditCombo('TEST'))
        self.main_page.layout().addWidget(self.rhs_bar)

        # Insert the main_page in to the stack
        self.stack.insertWidget(2, self.main_page)

        # Show GUI
        self.show()

    def login_clicked(self):
        self.db = DB()
        res = self.db.execute_read_query("SELECT * FROM users WHERE username = '%s';" % self.username_widget.get_text())
        if not res:
            self.stack.setCurrentIndex(1)
            self.db.execute_query("INSERT INTO users VALUES('%s', '%s', '%s');" % (self.create_user_page.get_usn_text(),
                                                                                   self.create_user_page.get_pwd_text(),
                                                                                   self.create_user_page.get_email_text()
                                                                                   )
                                  )
        else:
            print(res)




class Communicate(QObject):

    closeApp = pyqtSignal()


def main():
    app = QApplication([])
    mw = MainWindow()
    app.exec_()


if __name__ == '__main__':
    main()
