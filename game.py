import time
import json
import datetime

class game:
    def __init__(self,user):
        self.converted_time_total=user.TIME
        self.starting_time()

    def starting_time(self):
        self.startingtime=time.time()

    def ending_time(self):
        self.endingtime=time.time()

    def total_time(self):
        self.totaltime=round(self.startingtime-self.endingtime)
        self.converted_time=datetime.timedelta(seconds=self.totaltime)
        return self.converted_time


    
    def show_word(self):
        
        with open('word_list.json', 'r') as json_file:
          data = json.load(json_file)
          level=self.user_level
          for j in data[level]:
              print("h:",j)
              print("e",data[level][j])