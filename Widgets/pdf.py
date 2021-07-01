from PyQt5.QtWidgets import QApplication
import qpageview
import sys

app = QApplication(sys.argv)

v = qpageview.View()
v.loadPdf("resources/PDFs/dummy.pdf")
v.resize(900, 500)
v.show()

sys.exit(app.exec_())