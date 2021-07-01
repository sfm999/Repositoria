from resources.qt_resources.qt_widgets import *
from resources.qt_resources.qt_core import *
from resources.qt_resources.qt_gui import *
from Widgets.LineEditCombo import LineEditCombo
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create outer layout
        outer_layout = QVBoxLayout()

        # Create a top layout for top area
        top_layout = QVBoxLayout()

        top_layout.addWidget(LineEditCombo('Top Test 1'))
        top_layout.addWidget(LineEditCombo('Top Test 2'))
        top_layout.addWidget(LineEditCombo('Top Test 3'))

        middle_layout = QHBoxLayout()

        middle_layout.addWidget(LineEditCombo('Middle Test 1: '))
        middle_layout.addWidget(LineEditCombo('Middle Test 2: '))
        middle_layout.addWidget(LineEditCombo('Middle Test 3: '))

        bottom_layout = QHBoxLayout()

        bottom_layout.addWidget(QCheckBox('Bottom Test 1:'))
        bottom_layout.addWidget(QCheckBox('Bottom Test 2:'))
        bottom_layout.addWidget(QCheckBox('Bottom Test 3:'))

        outer_layout.addLayout(top_layout)
        outer_layout.addLayout(middle_layout)
        outer_layout.addLayout(bottom_layout)

        self.setLayout(outer_layout)


if __name__ == '__main__':
    q_app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    sys.exit(q_app.exec_())
