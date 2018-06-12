import time
import csv
import json
import os.path
import multifileTest
#TODO: clean up functions
#TODO: comment each function
#TODO: Create a list of functionalities that this program will achieve
#TODO: Seperate user and API data into two different lists
#TODO: Create another python file that will handle emailing/texting alerts
#TODO: Include 5 day moving average prediction
#will record stock bought, price, quantity, average price, etc

#addStocks will allow users to add the stock they are adding to their portfolio
#This information includes the name of the stock, the price they bought it at,
#The quantity they bought,
#
def addStocks(data, name, price, quantity):
	data["stocks"].append({
		"name" : name, #name of the stock
		"quantity" : quantity, #amount of shares you are buying
		"bought price" : cost, #The price of a single share
		"current price" : "x", #AlphaVantage data - current price of a single share 
		"percent change" : "x", #alphaVantage data calculation - percent change from user data ((current price - bought price  )/bought price)
		"notification" :"false", # allow the program to send email/ text alerts to user
		"watch price": "x", #watch price indicates the price to notify and sell at.
		"watch percent" : "x" #watch percent indicates the positive percent to notify and sell at
		#TODO: maybe include volume as well
		})

	with open('data.json', 'w') as outfile:
		json.dump(data, outfile)

	jsonData = json.dumps(data)
	#print(jsonData)
	return data

def printJson():
	with open('data.json') as json_file:
		data = json.load(json_file)
		
		for p in data["stocks"]:		
			print('name: '+ p['name'])
			print('current Price: '+ p['current price'])


def initCreateJson():
	data = {}
	username = input("Enter your name: ")
	age = input("Enter your age: ")
	data["user"] = []
	data["stocks"] = []
	data["user"].append({
		"username" : username,
		"age" : age
		})

	with open('data.json', 'w') as outfile:
		json.dump(data, outfile)
	
	print("Please enter in some stocks you want to track below.")
	numberofStocks = input("how many stocks do you want to add: ")

	for i in range(int(numberofStocks)):
		name = input("Enter the name of the stock: ")
		quantity = input("Enter the amount of " + name + " you bought: ")
		price = input("Enter the cost of 1 share of " + name + ": ")

	addStocks(data,price,name, quantity) #use the function defined to add stocks to data.json file
		

	


def loadJson():
	with open('data.json','r') as infile:
		data = json.load(infile)
	return data

def menu(data):
	print("Welcome to the menu.")
	print(
		"1)Print stock information. \n" + 
		"2)add a stock. \n" +
		"3)remove a stock \n" +
		"4)set notifications"
		 )
	print()
	choice = input("Please select an option.")
	if(choice == 1):
		stockInfo(data)

def stockInfo(data):
	print("My stocks information.")

def main(): 
	#data = createJson()
	# addStocks(data, 'tsla', '90', '100')
	# addStocks(data, 'spyerdo','100', '12312')
	# printJson()
	
	print("Welcome to Kent's Stock Portfolio Tracker.")
	
	#check to see if data file exists
	if(os.path.isfile("data.json")== False):
		initCreateJson()
	data = loadJson() 
	menu(data)

	#print(json.dumps(data,indent=4, sort_keys=True))
	#multifileTest.sayHello()
if __name__ == "__main__": main()