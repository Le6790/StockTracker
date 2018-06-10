import json
#I will basically be using a python dictionary of lists for storing stock data. 

data = {}
data["stocks"] = []
data["stocks"].append({
	'name': 'aapl',
	'current price': '191.70',
	'quantity' : '100',
	'bought average' : '190.00' 
	})
data["stocks"].append({
	'name': 'tsla',
	'current price': '1',
	'quantity' : '10000',
	'bought average' : '124310.00' 
	})
#change key in dictionary
#data["stocks"][0]["name"] = "tsla"
#print(len(data["stocks"]))

#new data "category" list element
data["test"] = []
data["test"].append({
	'name': 'TEST',
	'current price': '1234',
	'quantity' : '098',
	'bought average' : '121414' 
	})


###Deleting a stock and all of its information###
for i in range(len(data["stocks"])):
	#print(i)
	if (data["stocks"][i-1]["name"] == "tsla"):
		del data["stocks"][i-1]
###Deleting a stock###


#del data["stocks"][0]


#print(data["stocks"]["name"])

#write json data to a file
with open('jsonTest.json', 'w') as outfile:
		json.dump(data, outfile)


#read json file and store it in a variable
with open('jsonTest.json','r') as infile:
	inJson = json.load(infile)
#pretty print JSON data 
print(json.dumps(inJson, indent=4, sort_keys=True))

