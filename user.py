from PyQt5 import QtWidgets,uic
import json
import os

class users:
    
    def __init__(self,name,level=1,totalTime=0):
        self.name=name
        self.level=level
        self.totalTime=totalTime

    def search(self):
        
        if os.path.exists(self.name+'.json'):
           self.login()
        else:    
           self.signUp()

    def signUp(self):
        myDict = {
        "name": self.name,
        "level":self.level ,
        "totalTime":self.totalTime,
         }
        
        with open(self.name+'.json', 'w') as json_file:
            json.dump(myDict, json_file,indent=4)

        self.login()

    def login(self):
        with open (self.name+'.json','r') as json_file:
            data=json.load(json_file)
            self.level=data["level"]
            self.totalTime=data["totalTime"]
        #print("OK")
       
        
    def register(self,lastlevel,passedTime):
        my_file = open(self.name+'.json', "r")
        data = json.load(my_file)
        my_file.close()
        #print(data)
        data["level"] = lastlevel
        self.level=lastlevel
        data["totalTime"]+=passedTime
        my_file= open(self.name+'.json', "w")
        json. dump(data, my_file,indent=4)
        my_file.close()
        return data

              

        


