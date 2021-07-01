from resources.qt_resources.qt_widgets import *
from PyQt5.QtGui import QFont


class LineEditCombo(QWidget):
    def __init__(self, label_text):
        super().__init__()

        # Create label and input
        self.lbl = QLabel(label_text)
        self.lbl.setFont(QFont('Helvetica [Cronyx]', 10, QFont.StyleItalic))
        self.inp = QLineEdit()

        # Set the layout as HBox so the widgets go next to each other and not stacked on each other vertically
        self.setLayout(QHBoxLayout())

        # Add the widgets to the layout.
        self.layout().addWidget(self.lbl)
        self.layout().addWidget(self.inp)

        # Show the widget
        self.show()

    def get_text(self):
        return self.inp.text()