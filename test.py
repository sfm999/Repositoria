from Widgets.LoginPage import LoginPage
from resources.qt_resources.qt_widgets import *
import sys



if __name__ == "__main__":
    app = QApplication(sys.argv)    # <---
    window = LoginPage()
    sys.exit(app.exec_())

