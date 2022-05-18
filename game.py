import json
import time

class game_play():
    def __init__(self,obj):
        self.obj=obj
        self.true_num=0
        self.false_num = 0
        self.timer=0
        self.total_try=0
        self.word_list = self.words()
        
    def starting_time(self):
        self.start_time=time.time()
        return self.start_time

    def total_time(self,start_time):
        self.start_time=start_time
        self.end_time=time.time()
        self.totaltime=self.end_time-self.start_time
        return int(self.totaltime)
 
    def words(self):
        self.level= self.obj.level
        with open('word_list.json', 'r') as json_file:
           words=[]
           data= json.load(json_file)
           for j in data[str(self.level)]:
              n_e=[]
              n_e.append(j)
              n_e.append(data[str(self.level)][j])
              words.append(n_e)
        return words
    
    def show_word(self):
        if self.true_num==20:
            self.obj.level=self.obj.level+1
            self.obj.registerLevel(self.obj.level)
            self.word_list = self.words()
            self.true_num=0
            self.total_try=0
        self.nl=self.word_list[self.true_num][0]
        self.en=self.word_list[self.true_num][1]
        return self.nl,self.en,self.true_num

    def total_try_num(self):
        self.total_try=self.total_try+1 
        return self.total_try
    
    def true(self):
        self.true_num+=1

    def false(self):
        self.false_word=self.word_list.pop( self.true_num)
        self.word_list.append(self.false_word)
        #print(self.word_list)
        

    