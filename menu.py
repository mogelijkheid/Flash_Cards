from PyQt5 import QtWidgets,uic
import login
import play
import game
import user

class menu_window(QtWidgets.QMainWindow):
    
    def __init__(self,obj):
        self.obj=obj
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
        self.cams = play.play_window(self.obj)
        self.word_nl, self.word_en=game.game_play().show_word(self.obj.level)
        self.cams.level_label.setText("LEVEL "+str(self.obj.level))
        self.cams.languages.setText("NEDERLANDS")
        self.cams.words.setText(self.word_nl[0])
        self.cams.show()
        self.close()