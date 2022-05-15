import json
from user import users
i=1
import time
import datetime
class game_play():
    
    def __init__(self):
        self.timer=0
        
    
    def starting_time(self):
        self.startingtime=time.time()

    def ending_time(self):
        self.endingtime=time.time()
        game_play.total_time()

    def total_time(self):
        self.totaltime=round(self.startingtime-self.endingtime)
        self.converted_time=datetime.timedelta(seconds=self.totaltime)
        return self.converted_time
    
    def show_word(self,level):
        self.nl=[]
        self.en=[]
        self.level=level
        with open('word_list.json', 'r') as json_file:
            data = json.load(json_file)
            i=0
            for j in data[str(self.level)]:
                if i<20:
                    self.nl.append(j)
                    self.en.append(data[str(self.level)][j])
                    i=i+1
        return self.nl, self.en

    
    
    def true(self,obj):
        global i
        self.obj=obj
        if i==20:
            self.obj.level=self.obj.level+1
            obj.register(self.obj.level,555)
            i=0
        self.word_nl,self.word_en=game_play().show_word(self.obj.level)
        self.nl=self.word_nl[i]
        self.en=self.word_en[i]
        i=i+1
        # total_seconds = 3
        # while total_seconds >= 0:
        #     timer = datetime.timedelta(seconds = total_seconds)
        #     print(timer, end="\r")
        #     time.sleep(1)
        #     total_seconds -= 1
        return self.nl, self.en, i-1
            
    
    # def false(self):
    #     global i
    #     self.false_nl=[]
    #     self.false_en=[]
    #     self.level=1
    #     if i==20:
    #         level=level+1
    #         i=0
    #     self.word_nl,self.word_en=game_play().show_word(self.level)
    #     self.nl=self.word_nl[i]
    #     self.en=self.word_en[i]
    #     self.false_nl=self.nl
    #     self.false_en=self.false_en
    #     i=i+1
    #     # total_seconds = 3
    #     # while total_seconds >= 0:
    #     #     timer = datetime.timedelta(seconds = total_seconds)
    #     #     print(timer, end="\r")
    #     #     time.sleep(1)
    #     #     total_seconds -= 1
    #     return self.nl, self.en



