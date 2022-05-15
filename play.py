from PyQt5 import QtWidgets,uic
import menu
import game
from game import game_play



class play_window(QtWidgets.QMainWindow):
    
    def __init__(self,obj):
        self.obj=obj
        super(play_window, self).__init__()
        uic.loadUi('ui/play.ui', self)
        self.back_button.clicked.connect(self.menu_show)
        self.exit_button.clicked.connect(self.exit)
        
        self.true_button.clicked.connect(self.change) 
        #self.false_button.clicked.connect()
        self.show()
        
    def menu_show(self):
        self.cams=menu.menu_window(self.obj)
        self.cams.welcome_label.setText("WELCOME "+str(self.obj.name))
        self.cams.level_label.setText("LEVEL "+str(self.obj.level))
        self.cams.total_time_label.setText("TOTAL TIME "+str(self.obj.totalTime))
        self.cams.show()
        self.close()
        
    def exit(self):
        self.close()
        
    
    def change(self):
        self.word_nl, self.word_en, self.trueScore=game.game_play().true(self.obj)
        self.languages.setText("NEDERLANDS")
        self.true_score.setText(str(self.trueScore))
        self.level_label.setText("LEVEL "+str(self.obj.level))
        self.words.setText(self.word_nl)
        
        # self.words.setText(self.word_en)
        
    
       
        

