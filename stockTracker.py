import json
import getTime
import alphaStocks as alpha
def loadJson():
	with open('data.json','r') as infile:
		data = json.load(infile)
	return data

def saveJson(data):
	with open('data.json', 'w') as outfile:
		json.dump(data, outfile)

#addStocks will allow users to add the stock they are adding to their portfolio
#This information includes the name of the stock, the price they bought it at,
#The quantity they bought,
def addStocks(data, name, price, quantity):
	data["stocks"].append({
		"name" : name, #name of the stock
		"quantity" : quantity, #amount of shares you are buying
		"bought price" : price, #The price of a single share
		"current price" : "x", #AlphaVantage data - current price of a single share 
		"percent change" : "x", #alphaVantage data calculation - percent change from user data ((current price - bought price  )/bought price)
		"notification" :"false", # allow the program to send email/ text alerts to user
		"watch price": "x", #watch price indicates the price to notify and sell at.
		"watch percent" : "x" #watch percent indicates the positive percent to notify and sell at
		#TODO: maybe include volume as well
		})

	saveJson(data)

	jsonData = json.dumps(data)
	#print(jsonData)
	return data 

#get data (json object) as parameter, delete the selected stock, and save
def deleteStocks(data):
	
	for i in range(len(data["stocks"])):
		#print(i)
		if (data["stocks"][i-1]["name"] == "tsla"):
			del data["stocks"][i-1]

	saveJson(data)


def updateStocks(data):
	currentPrice =""
	percentChange = ""

	if getTime.isMarketOpen() == False:
		currentTime = getTime.getCurrentDate() + " 16:00:00"
		#print(closeTime)
	else: 
		currentTime = getTime.getCurrentTime()
		
	for i in range(len(data["stocks"])):
		IntradayData = alpha.getIntraday(data["stocks"][i]["name"])
		currentPrice = float(IntradayData["Time Series (1min)"][currentTime]["1. open"])
		currentPrice = "%.2f" % currentPrice
		

	saveJson(data)
