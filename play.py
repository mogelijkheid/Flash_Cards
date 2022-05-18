from PyQt5 import QtWidgets,uic
from PyQt5.QtCore import QTimer
import menu
import game
from game import game_play

class play_window(QtWidgets.QMainWindow):
    
    def __init__(self,obj,start_time):
        self.obj=obj
        self.start_time=start_time
        super(play_window, self).__init__()
        uic.loadUi('ui/play.ui', self)
        self.game_obj = game.game_play(self.obj)
        self.true_button.setEnabled(False)
        self.false_button.setEnabled(False)
        self.back_button.clicked.connect(self.menu_show)
        self.exit_button.clicked.connect(self.exit)
        self.true_button.clicked.connect(self.true_button_function) 
        self.false_button.clicked.connect(self.false_button_function)
        self.timer_()
        self.show()
        
    def menu_show(self):
        self.cams=menu.menu_window(self.obj)
        self.passedTime=int(self.game_obj.total_time(self.start_time))
        self.obj.registerTime(self.passedTime)
        self.cams.welcome_label.setText("WELCOME "+str(self.obj.name).upper())
        self.cams.level_label.setText("LEVEL "+str(self.obj.level))
        self.cams.total_time_label.setText("TOTAL TIME "+self.obj.totalTime)
        self.cams.level_progressbar.setProperty('value',self.progress_bar())
        self.cams.show()
        self.close()
        
    def progress_bar(self):
        return (self.obj.level/250)*100
           
    def update(self):
        self.timer_label.setText(str(self.count))
        if self.count == 0:
            self.true_button.setEnabled(True)
            self.false_button.setEnabled(True)
            self.timer.stop()
            self.en_word(self.word_en)
        self.count -= 1
            
    def en_word(self,en):
        self.en=en
        self.languages.setText("ENGLISH")
        self.cards.setStyleSheet("background-color: rgb(255, 255, 220);\nborder-color: rgb(170, 85, 0);\nborder-style: solid;\nborder-width: 3px;\nborder-radius:50px;")
        self.words.setText(self.en)
        
    def timer_(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)
        self.count = 3
        self.starting()
        
    def false_word(self):
        self.totalTry_num=self.game_obj. total_try_num()
        self.total_try.setText(str(self.totalTry_num))                                                                   
    
    def starting(self):
        self.word_nl, self.word_en,self.true_num=self.game_obj.show_word()
        self.totalTry_num=self.game_obj.total_try
        self.cards.setStyleSheet("background-color:rgb(5, 119, 161);\nborder-color: rgb(170, 85, 0);\nborder-style: solid;\nborder-width: 3px;\nborder-radius:50px;")
        self.level_label.setText("LEVEL "+str(self.obj.level))
        self.languages.setText("NEDERLANDS")
        self.true_score.setText(str(self.true_num))
        self.words_level.setProperty('value',self.true_num)
        self.true_button.setEnabled(False)
        self.false_button.setEnabled(False)
        self.words.setText(self.word_nl)
        self.total_try.setText(str(self.totalTry_num))
    
    def true_button_function(self):
        self.game_obj.total_try_num()
        self.game_obj.true()
        self.timer_()
        
    def false_button_function(self):
        self.game_obj.total_try_num()
        self.game_obj.false()
        self.timer_()
           
    def exit(self):
        self.passedTime=self.game_obj.total_time(self.start_time)
        self.obj.registerTime(self.passedTime)
        self.close()
        

