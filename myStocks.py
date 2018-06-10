import time
import csv
import json
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
	print(jsonData)

def printJson():
	with open('data.json') as json_file:
		data = json.load(json_file)
		
		for p in data["stocks"]:		
			print('name: '+ p['name'])
			print('current Price: '+ p['current price'])


def main():
	data = {}
	data["stocks"] = []
	data["stocks"].append({
		'name': 'aapl',
		'current price': '191.70',
		'quantity' : '100',
		'bought average' : '190.00' 
		})

	with open('data.json', 'w') as outfile:
		json.dump(data, outfile)
	addStocks(data, 'tsla', '90', '100')

	printJson()

if __name__ == "__main__": main()