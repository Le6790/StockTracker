import time
import csv
import json
import os.path
from threading import Thread
import getTime
import stockTracker
#TODO: clean up functions
#TODO: comment each function
#TODO: Create a list of functionalities that this program will achieve
#TODO: Seperate user and API data into two different lists
#TODO: Create another python file that will handle emailing/texting alerts
#TODO: Include 5 day moving average prediction

#TODO: ADD redudency checks to data inputs
#will record stock bought, price, quantity, average price, etc


#main file


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

	stockTracker.saveJson(data)
	
	print("Please enter in some stocks you want to track below.")
	numberofStocks = input("how many stocks do you want to add: ")

	for i in range(int(numberofStocks)):
		name = input("Enter the name of the stock: ")
		quantity = input("Enter the amount of " + name + " you bought: ")
		price = input("Enter the cost of 1 share of " + name + ": ")
		stockTracker.addStocks(data) #use the function defined to add stocks to data.json file
		



def menu(data):
	print("Welcome to the menu.")
	print(
		"1)Print stock information. \n" + 
		"2)add a stock. \n" +
		"3)remove a stock \n" +
		"4)set notifications\n" + 
		"q) quit"
		 )
	print()
	choice = input("Please select an option.")
	if(choice == "q"):
		exit()
	if(choice == "1"):
		stockInfo(data)
	if(choice == "2"):
		stockTracker.addStocks(data)
	if(choice == "3"):
		stockTracker.deleteStocks(data)

def stockInfo(data):
	#stockTracker.updateStocks(data)
	stockTracker.printStockData(data)

def main(): 
	#data = createJson()
	# addStocks(data, 'tsla', '90', '100')
	# addStocks(data, 'spyerdo','100', '12312')
	# printJson()

	print("Welcome to Kent's Stock Portfolio Tracker.")
	if(getTime.isMarketOpen() == True): #TODO: Delete
		print("Looks like the market is open right now!")
		print(getTime.getCurrentTime())
	else:
		print("The market is currently closed.")
		print(getTime.getCurrentTime())

	#check to see if data file exists
	if(os.path.isfile("data.json")== False):
		initCreateJson()
	data = stockTracker.loadJson() 


	while (1):
		update=Thread(target=stockTracker.updateStocks,args=(data,))
		update.start()
		if update.isAlive():
			menu(data)

	#print(json.dumps(data,indent=4, sort_keys=True))
	#multifileTest.sayHello()
if __name__ == "__main__": main()