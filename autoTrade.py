#This is meant to automate steam market trades
from os import system
import requests
import json
import time
#retrieves json file from market
def getJson(url,name,el):
    jFile = requests.get(url)
    jString = jsonToString(jFile)
    print(name)
    print(parseString(jString,el))
#converts json file to string ready to be manipulated
def jsonToString(jFile):
    jString = str(jFile.json())
    return jString
#seperates elements of string from json file
def parseString(jsonString,item):
    print("parse out wanted values from returned string received from steam...")
    lowestPrice = ""
    volume = ""
    medianPrice =""
    time.sleep(2)
    jString = jsonString
    el=0
    for i in range(0,len(jString)):
    
        #if(jString[i]==","):
        match el:
            case 0:
                lowestPrice = lowestPrice + jString[i]
                   

            case 1:
                volume = volume + jString[i]
                    

            case 2:
                medianPrice = medianPrice + jString[i]
                
        if(jString[i]==","):
            el+=1
            

    #jString = lowestPrice+" "+volume+" "+medianPrice
    return jString


#reads file that contains urls for item to retieve info for
def itemFileRead():
    f = open('itemsLocations.json','r')
    f=f.read()
    f=json.loads(f)
    return f
#
def itemValue(f):
    x=0
    for i in range(3):
        name =f['item'][x]['Name']
        url =f['item'][x]['url']
        getJson(url,name,i)
        x+=1
_ = system("clear")
print("<<<Steam Market Script 1.0>>>")
print("Starting....\n")

itemValue(itemFileRead())
