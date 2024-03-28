from os import system
import requests
import json
import time
#retrieves json file from market
def getJson(url,name):
	jFile = requests.get(url)
	jFile = jFile.json()
	fail = jFile["success"]	

	#check if request failed or passed 
	if fail=="False":
		print(jFile["success"])
	else:
		print(name)
		print(parseJSON(jFile)+"\n")

#seperates elements of string from json file
def parseJSON(jString):
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

#get individual values from the JSON file(lowestPrice, volume, and medianPrice)
def get_lowest_price():
	jFile = requests.get('https://steamcommunity.com/market/priceoverview/?country=CA&currency=20&appid=730&market_hash_name=SCAR-20%20%7C%20Poultrygeist%20%28Field-Tested%29')
	jFile = jFile.json()	
	lowest = jFile['lowest_price']
	return lowest
def get_volume():
	jFile = requests.get('https://steamcommunity.com/market/priceoverview/?country=CA&currency=20&appid=730&market_hash_name=SCAR-20%20%7C%20Poultrygeist%20%28Field-Tested%29')
	jFile = jFile.json()	
	volume = jFile['volume']
	return volume
def get_median_price():
	jFile = requests.get('https://steamcommunity.com/market/priceoverview/?country=CA&currency=20&appid=730&market_hash_name=SCAR-20%20%7C%20Poultrygeist%20%28Field-Tested%29')
	jFile = jFile.json()
	median = jFile['median_price']

	return median

#Main
_ = system("clear")
print("<<<Steam Market Script 1.0>>>")
print("Starting....\n")

itemValue(itemFileRead())
