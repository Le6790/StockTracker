import requests
import matplotlib.pyplot as plt
import json
import time

def getRequest(avUrl, params):
    req = requests.get(url = avUrl, params= params)
    return req

def getCurrentTime():
    localtime = time.localtime(time.time())
    year = str(localtime[0])
    month = str(localtime[1])
    day = str(localtime[2])
    hourEST = str(localtime[3]+2) # from MST to EST
    minute = str(localtime[4])
    second = '00'
    currentTime = '%s-%s-%s %s:%s:%s' %(year, month, day, hourEST, minute, second)
    currentTime = str(localtime[0]) + '-' + str(localtime[1]) +'-' + str(localtime[2]) + ' ' + str(localtime[3]) + ':' + str(localtime[4]-2) + ':00' 
    
    timeList = []
    
    for i in range(0,10):
        if localtime[3]+i < 10:
            hourEst = 0 + str(localtime+i)
        else:
            hourEst = str(localtime[3]+i)
        currentTime = '%s-%s-%s %s:%s:%s' %(year, month, day, hourEST, minute, second)
        timeList.append(currentTime)
    print(currentTime)
    print(timeList)


def main():
    
    avUrl = 'https://www.alphavantage.co/query?'
    params = dict(
    function = 'TIME_SERIES_INTRADAY',
    symbol = 'MSFT',
    interval = '1min',
    outputSize = 'compact',
    apikey = 'BZU2NV9X6TBDG3KG' #pures APIKEY
    )

    # req = getRequest(avUrl, params)
    # print(req.status_code)
    # print(req.text)
    # jsonData = req.json()
    # print(map(int, jsonData.keys()))
    
    getCurrentTime()
    

if __name__ == "__main__": main()
