import time 
def getCurrentTime():
    localtime = time.localtime(time.time())
    year = str(localtime[0])
    month = '%02d' % localtime[1]
    day = str(localtime[2])
    hourEST = str(localtime[3]+2) # from MST to EST
    if (int(hourEST) > 2):
        hourEST = str(int(hourEST) % 24)
    
    minute = str(localtime[4])
    second = '00'
    currentTime = '%s-%s-%s %s:%s:%s' %(year, month, day, hourEST, minute, second)
    #currentTime = str(localtime[0]) + '-' + str(localtime[1]) +'-' + str(localtime[2]) + ' ' + str(localtime[3]) + ':' + str(localtime[4]-2) + ':00' 
    
    timeList = []
    
    for i in range(0,10):
        if localtime[3]+i < 10:
            hourEst = 0 + str(localtime+i)
        else:
            hourEst = str(localtime[3]+i)

        currentTime = '%s-%s-%s %s:%s:%s' %(year, month, day, hourEST, minute, second)
        timeList.append(currentTime)
    #print(currentTime)
    #print(timeList)

    return currentTime

def getCurrentDate():
    localtime = time.localtime(time.time())
    year = str(localtime[0])
    month = '%02d' % localtime[1]
    day = str(localtime[2])

    currentDate = "%s-%s-%s" %(year, month, day)
    return currentDate

def isMarketOpen():
    localtime = time.localtime(time.time())
    hourEST = str(localtime[3]+2)
    if (int(hourEST) > 24):
        hourEST = str(int(hourEST) % 24)
    minute = str(localtime[4])
    print("EST hour is: " + hourEST +":"+ minute)
    if (int(hourEST) >= 9 and int(hourEST) < 16):
        if (int(hourEST == 9) and (int(minute) <=30)):
            print("Market is not open. Please check again at 9:30")
            return False
        print("Market is open.")
        return True
    print("market is not open.")
    return False


# def getCurrentTime():
#     localtime = time.localtime(time.time())
#     year = str(localtime[0])
#     month = str(localtime[1])
#     day = str(localtime[2])
#     hourEST = str(localtime[3]+2) # from MST to EST
#     minute = str(localtime[4])
#     second = '00'
#     currentTime = '%s-%s-%s %s:%s:%s' %(year, month, day, hourEST, minute, second)
#     currentTime = str(localtime[0]) + '-' + str(localtime[1]) +'-' + str(localtime[2]) + ' ' + str(localtime[3]) + ':' + str(localtime[4]-2) + ':00' 
    
#     timeList = []
    
#     for i in range(0,10):
#         if localtime[3]+i < 10:
#             hourEst = 0 + str(localtime+i)
#         else:
#             hourEst = str(localtime[3]+i)
#         currentTime = '%s-%s-%s %s:%s:%s' %(year, month, day, hourEST, minute, second)
#         timeList.append(currentTime)
#     print(currentTime)
#     print(timeList)