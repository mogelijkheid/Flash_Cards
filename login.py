from PyQt5 import QtWidgets,uic
import menu
from logo import logo_rc
import aboutus 


class login_window(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(login_window, self).__init__()
        uic.loadUi('ui/login.ui', self)
        self.enter_button.clicked.connect(self.menu_show)
        self.about_us_button.clicked.connect(self.aboutus_show)
        self.show()
        
    def menu_show(self):
        self.cams=menu.menu_window()
        self.cams.show()
        self.close()
        
    def aboutus_show(self):
        self.cams=aboutus.aboutus_window()
        self.cams.show()