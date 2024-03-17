#This is meant to automate steam market trades
from os import system
import requests
import json
import time
#retrieves json file from market
def getJson(url,name):
	jFile = requests.get(url)
	jFile = jFile.json()
	print(name)
	print(parseString(jFile)+"\n")

#seperates elements of string from json file
def parseString(jString):
	print("parse out wanted values from returned string received from steam...")
	
	lowestPrice = jString["lowest_price"]
	volume = jString["volume"]
	medianPrice = jString["median_price"]
	time.sleep(2)
            

	jString ="Lowest Price: "+ lowestPrice+", Volume: "+" "+volume+", Median Price: "+" "+medianPrice
	return jString



#reads file that contains urls for item to retieve info for
def itemFileRead():
	f = open('itemsLocations.json','r')
	f=f.read()
	f=json.loads(f)
	return f
#gets values from json file in directory 
def itemValue(f):
	x=0
	for i in range(3):
		name =f['item'][x]['Name']
		url =f['item'][x]['url']
		getJson(url,name)
		x+=1
#Main
_ = system("clear")
print("<<<Steam Market Script 1.0>>>")
print("Starting....\n")

itemValue(itemFileRead())
