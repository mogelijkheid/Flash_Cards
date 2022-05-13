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


