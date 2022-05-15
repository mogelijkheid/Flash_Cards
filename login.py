from PyQt5 import QtWidgets,uic
import menu
from logo import logo_rc
import aboutus 
import user



class login_window(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(login_window, self).__init__()
        uic.loadUi('ui/login.ui', self)
        self.enter_button.clicked.connect(self.create)
        self.about_us_button.clicked.connect(self.aboutus_show)
        self.show()
        
    def create(self):
        a=user.users(self.username_line.text())
        a.search() 
        self.menu_show(a)
        
    def menu_show(self,obj):
        self.obj=obj
        self.cams=menu.menu_window(self.obj)
        self.cams.welcome_label.setText("WELCOME "+str(self.obj.name))
        self.cams.total_time_label.setText("TOTAL TIME "+str(self.obj.totalTime))
        self.cams.level_label.setText("LEVEL "+str(self.obj.level))
        self.cams.show()
        self.close()
        
    def aboutus_show(self):
        self.cams=aboutus.aboutus_window()
        self.cams.show()