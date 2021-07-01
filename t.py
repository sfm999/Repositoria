from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralWidget)

        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start_button = QtWidgets.QPushButton(self.centralWidget)
        self.start_button.setObjectName("start_button")

        self.horizontalLayout.addWidget(self.start_button)
        self.stop_button = QtWidgets.QPushButton(self.centralWidget)
        self.stop_button.setObjectName("stop_button")
        self.horizontalLayout.addWidget(self.stop_button)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 26))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)


stylesheet = """
    QMainWindow {
        background-image: url("resources/images/books1.png"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(stylesheet)

    w = MyWindow()
#   MainWindow = QtWidgets.QMainWindow()
#   ui = Ui_MainWindow()
#   ui.setupUi(MainWindow)
#   MainWindow.show()
    w.show()

    sys.exit(app.exec_())


    """
    self.setWindowTitle('Repositoria | Login Page')
        self.resize(600, 500)

        self.background_widget = QWidget()
        self.background_widget.setObjectName('BackgroundWidget')

        self.h_layout = QHBoxLayout(self.background_widget)
        self.h_layout.setObjectName('BackgroundHLayout')
        self.h_layout.setContentsMargins(11, 11, 11, 11)
        self.h_layout.setSpacing(6)

        self.menu_bar = QMenuBar()

        # Set login_page layout to vertical layout
        self.setLayout(QVBoxLayout())

        # Create the label/input combo widgets
        self.username_widget = LineEditCombo('Username: ')
        self.password_widget = LineEditCombo('Password: ')
        self.password_widget.inp.setEchoMode(QLineEdit.Password)

        # Add the widgets to the layout of the login_page
        self.layout().addWidget(self.username_widget)
        self.layout().addWidget(self.password_widget)

        # Create the login and exit buttons
        login_btn = QPushButton('Login')

        # Add the buttons to the layout
        self.layout().addWidget(login_btn)

        # Setup up on click signal for logging in
        login_btn.clicked.connect(self.login_clicked)

        # Show GUI
        self.show()
        """