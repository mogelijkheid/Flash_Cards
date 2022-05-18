from PyQt5 import QtWidgets,uic
import login
import play
import game

class menu_window(QtWidgets.QMainWindow):
    
    def __init__(self,obj):
        self.obj=obj
        self.game_obj = game.game_play(self.obj)
        super(menu_window, self).__init__()
        uic.loadUi('ui/menu.ui', self)
        self.welcome_label.setText("WELCOME "+str(self.obj.name).upper())
        self.total_time_label.setText("TOTAL TIME "+self.obj.totalTime)
        self.level_label.setText("LEVEL "+str(self.obj.level))
        self.level_progressbar.setProperty('value',self.progress_bar(obj))
        self.logout_button.clicked.connect(self.login_window_show)       
        self.play_button.clicked.connect(self.play_window_show)
        self.show()
    
    def login_window_show(self):
        self.cams = login.login_window()
        self.cams.show()
        self.close()
    
    def play_window_show(self):
        self.start_time=self.game_obj.starting_time()
        self.cams = play.play_window(self.obj,self.start_time)
        self.cams.show()
        self.close()
        
    def progress_bar(self,obj):
        self.obj=obj
        return (self.obj.level/250)*100