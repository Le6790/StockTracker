import json
import getTime
import alphaStocks as alpha
import time
#load the json file in
def loadJson():
	with open('data.json','r') as infile:
		data = json.load(infile)
	return data

#-----------------------------------------------

#save the json file
def saveJson(data):
	with open('data.json', 'w') as outfile:
		json.dump(data, outfile)

#-------------------------------------------------

#addStocks will allow users to add the stock they are adding to their portfolio
#This information includes the name of the stock, the price they bought it at,
#The quantity they bought,
def addStocks(data):
	name = input("Enter the name of the stock: ")
	quantity = input("Enter the amount of " + name + " you bought: ")
	price = input("Enter the cost of 1 share of " + name + ": ")

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
	updateOneStock(data, name)
	return data 

#get data (json object) as parameter, delete the selected stock, and save
def deleteStocks(data):
	name = input("Enter the stock you want to remove: ")
	isExists = False
	for i in range(len(data["stocks"])):
		#print(i)
		if (data["stocks"][i-1]["name"] == name):
			del data["stocks"][i-1]
			isExists = True
	if isExists == False:
		print("That stock is not in your portfolio.")
	saveJson(data)

#

def updateOneStock(data,name):
	count = -1
	for i in range(len(data["stocks"])):
		if name == data["stocks"][i]["name"]:
			count = i
	if count == -1:
		return
	else:
		currentPrice =""
		percentChange =""

		if getTime.isMarketOpen() == False:
			currentTime = getTime.getCurrentDate() + " 16:00:00"
			currentTime = "2018-07-03 13:00:00" #TODO REMOVE
		#print(closeTime)
		else: 
			currentTime = getTime.getCurrentTime()

		IntradayData = alpha.getIntraday(data["stocks"][count]["name"])
		currentPrice = float(IntradayData["Time Series (1min)"][currentTime]["1. open"])
		data["stocks"][count]["current price"] = str(currentPrice)

def updateStocks(data):
	time.sleep(30)
	currentPrice =""
	percentChange = ""

	if getTime.isMarketOpen() == False:
		currentTime = getTime.getCurrentDate() + " 16:00:00"
		currentTime = "2018-07-03 13:00:00" #TODO REMOVE
		#print(closeTime)
	else: 
		currentTime = getTime.getCurrentTime()
		
	for i in range(len(data["stocks"])):
		IntradayData = alpha.getIntraday(data["stocks"][i]["name"])
		currentPrice = float(IntradayData["Time Series (1min)"][currentTime]["1. open"])
		currentPrice = "%.2f" % currentPrice
		data["stocks"][i]["current price"] = str(currentPrice) #modify json data "current price"
		
	print("Done updating Stocks.")
	saveJson(data)


def printStockData(data):
	if getTime.isMarketOpen() == False:
		currentTime = getTime.getCurrentDate() + " 16:00:00"
		currentTime = "2018-07-03 13:00:00" #TODO REMOVE
		#print(closeTime)
	else: 
		currentTime = getTime.getCurrentTime()


	print("Todays stock data. ")
	for i in range(len(data["stocks"])):
		#IntradayData = alpha.getIntraday(data["stocks"][i]["name"]) #TODO make this automatic
		totalAmount = float(data["stocks"][i]["current price"]) * float(data["stocks"][i]["quantity"])
		print("---------------------------")
		print("Stock name: "+ data["stocks"][i]["name"])
		print("Current Price: "+ data["stocks"][i]["current price"])
		print("Bought Price: " + data["stocks"][i]["bought price"])
		print("quantity: " + data["stocks"][i]["quantity"])
		print("total amount: " + "%.2f" % totalAmount)
		print("---------------------------")
