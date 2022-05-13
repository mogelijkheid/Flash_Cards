from PyQt5 import QtWidgets,uic
import menu

class play_window(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(play_window, self).__init__()
        uic.loadUi('ui/play.ui', self)
        self.back_button.clicked.connect(self.menu_show)
        self.exit_button.clicked.connect(self.exit)
        #self.true_button.clicked.connect()
        #self.false_button.clicked.connect()
        self.show()
        
    def menu_show(self):
        self.cams=menu.menu_window()
        self.cams.show()
        self.close()
        
    def exit(self):
        self.close()
    
