from login import login_window
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = login_window()
app.exec_()