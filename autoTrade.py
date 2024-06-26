#TODO clean up code, make current code fit with current use case
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
#TODO reduce repeated code 
def get_lowest_price(name):

	match name:
		case 'Scar20.jpeg':	
			jFile = requests.get('https://steamcommunity.com/market/priceoverview/?country=CA&currency=20&appid=730&market_hash_name=SCAR-20%20%7C%20Poultrygeist%20%28Field-Tested%29')
			jFile = jFile.json()	
			lowest = jFile['lowest_price']
			return lowest
		
		case 'negev.jpeg':	
			jFile = requests.get("https://steamcommunity.com/market/priceoverview/?counrty=CA&currency=20&appid=730&market_hash_name=Negev%20%7C%20Ultralight%20%28Field-Tested%29")
			jFile = jFile.json()	
			lowest = jFile['lowest_price']
			return lowest
		
		case 'scout.jpeg':	
			jFile = requests.get('https://steamcommunity.com/market/priceoverview/?country=CA&currency=20&appid=730&market_hash_name=SSG%2008%20%7C%20Mainframe%20001%20%28Field-Tested%29')
			jFile = jFile.json()	
			lowest = jFile['lowest_price']
			return lowest
		
		case 'noPhoto.jpeg':		
			lowest = 'CDN$ 0.00'
			return lowest
		

def get_volume(name):
	match name:
		case 'Scar20.jpeg':
			jFile = requests.get('https://steamcommunity.com/market/priceoverview/?country=CA&currency=20&appid=730&market_hash_name=SCAR-20%20%7C%20Poultrygeist%20%28Field-Tested%29')
			jFile = jFile.json()	
			volume = jFile['volume']
			return volume
		
		case 'negev.jpeg':
			jFile = requests.get("https://steamcommunity.com/market/priceoverview/?counrty=CA&currency=20&appid=730&market_hash_name=Negev%20%7C%20Ultralight%20%28Field-Tested%29")
			jFile = jFile.json()	
			volume = jFile['volume']
			return volume
		
		case 'scout.jpeg':
			jFile = requests.get('https://steamcommunity.com/market/priceoverview/?country=CA&currency=20&appid=730&market_hash_name=SSG%2008%20%7C%20Mainframe%20001%20%28Field-Tested%29')
			jFile = jFile.json()	
			volume = jFile['volume']
			return volume
		
		case 'noPhoto.jpeg':	
			volume = '0'
			return volume
		


def get_median_price(name):
	
	match name:
		case 'Scar20.jpeg':
			jFile = requests.get('https://steamcommunity.com/market/priceoverview/?country=CA&currency=20&appid=730&market_hash_name=SCAR-20%20%7C%20Poultrygeist%20%28Field-Tested%29')
			jFile = jFile.json()
			median = jFile['median_price']

			return median
		
		case 'negev.jpeg':
			jFile = requests.get("https://steamcommunity.com/market/priceoverview/?counrty=CA&currency=20&appid=730&market_hash_name=Negev%20%7C%20Ultralight%20%28Field-Tested%29")
			jFile = jFile.json()
			median = jFile['median_price']

			return median
		
		case 'scout.jpeg':
			jFile = requests.get('https://steamcommunity.com/market/priceoverview/?country=CA&currency=20&appid=730&market_hash_name=SSG%2008%20%7C%20Mainframe%20001%20%28Field-Tested%29')
			jFile = jFile.json()
			median = jFile['median_price']

			return median
		
		case 'noPhoto.jpeg':
			median = 'CDN$ 0.00'
			return median

