from PyQt5 import QtWidgets,uic
import login
import play

class menu_window(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(menu_window, self).__init__()
        uic.loadUi('ui/menu.ui', self)
        self.logout_button.clicked.connect(self.login_window_show)
        self.play_button.clicked.connect(self.play_window_show)
        self.show()
    
    def login_window_show(self):
        self.cams = login.login_window()
        self.cams.show()
        self.close()
    
    def play_window_show(self):
        self.cams = play.play_window()
        self.cams.show()
        self.close()