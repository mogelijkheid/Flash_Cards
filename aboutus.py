from PyQt5 import QtWidgets,uic
from logo import logo_rc

class aboutus_window(QtWidgets.QDialog):
    
    def __init__(self):
        super(aboutus_window, self).__init__() 
        uic.loadUi('ui/aboutus.ui', self)
        self.ok_button.clicked.connect(self.exit)
        self.show()
        
    def exit(self):
        self.close()