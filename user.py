from PyQt5 import QtWidgets,uic
import json
import os
import datetime

class users:
    
    def __init__(self,name,level=1):
        self.name=name
        self.level=level
        self.totalTime="00:00:00"

    def search(self):
        if os.path.exists('users/{}.json'.format(self.name)):
           self.login()
        else:    
           self.signUp()

    def signUp(self):
        myDict = {
        "name": self.name,
        "level":self.level ,
        "totalTime":self.totalTime,
         }
        with open('users/{}.json'.format(self.name), 'w') as json_file:
            json.dump(myDict, json_file,indent=4)
        self.login()

    def login(self):
        with open ('users/{}.json'.format(self.name),'r') as json_file:
            data=json.load(json_file)
            self.level=data["level"]
            self.totalTime=data["totalTime"]
       
    def registerLevel(self,lastLevel):
        my_file = open('users/{}.json'.format(self.name), "r")
        data = json.load(my_file)
        my_file.close()
        #print(data)
        data["level"] = lastLevel
        self.level=lastLevel
        my_file= open('users/{}.json'.format(self.name), "w")
        json. dump(data, my_file,indent=4)
        my_file.close()
        return data
    
    def registerTime(self,passedTime):
        my_file = open('users/{}.json'.format(self.name), "r")
        data = json.load(my_file)
        my_file.close()
        #print(data)
        h, m, s = data["totalTime"].split(':')
        self.totaltime=int(h) * 3600 + int(m) * 60 + int(s)+passedTime
        self.converted_time=str(datetime.timedelta(seconds = self.totaltime))
        data["totalTime"]=self.converted_time
        self.totalTime=self.converted_time
        my_file= open('users/{}.json'.format(self.name), "w")
        json. dump(data, my_file,indent=4)
        my_file.close()
        return data

              


