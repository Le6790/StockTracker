import time
import csv
import json
import os.path
import multifileTest
#using csv to save my stock data
#or json?
#lets try both
#will record stock bought, price, quantity, average price, etc


def addStocks(data, name, price, quantity):
	data["stocks"].append({
		'name': name,
		'current price': price,
		'quantity' : quantity,
		'bought average' : price 
		})

	with open('data.json', 'w') as outfile:
		json.dump(data, outfile)

	jsonData = json.dumps(data)
	#print(jsonData)

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
	print("Please enter in some stocks you want to track below.")
	numberofStocks = input("how many stocks do you want to add: ")

	for i in range(int(numberofStocks)):
		name = input("Enter the name of the stock: ")
		quantity = input("Enter the amount of " + name + " you bought: ")
		cost = input("Enter the cost of the " + name + ": ")

		data["stocks"].append({
			"name" : name,
			"quantity" : quantity,
			"average cost" : cost,
			"current price" : "x",
			"percent change" : "x",
			"notification" :"false",
			"sell price": "x",
			"sell percent" : "x"

			})

	with open('data.json', 'w') as outfile:
		json.dump(data, outfile)


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