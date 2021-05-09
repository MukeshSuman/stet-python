import json

from req import login

userIds = []
dateList = []
loads = 0
userIdsIndex = 0
dateListIndex = 0
userIdsLen = 0
dateListLen = 0


with open("userIds.json") as user_file:
    data = json.load(user_file)
    userIds = data["userIds"]
    userIdsLen = len(userIds)
    loads = loads + 1

with open("dateListA.json") as date_file:
    data = json.load(date_file)
    dateList = data["dateList"]
    dateListLen = len(dateList)
    loads = loads + 1


def startFn():
    if userIdsLen and dateListLen:
        apiHit()


apiHitCount = 0


def apiHit():
    global apiHitCount
    global userIdsIndex
    global dateListIndex
    apiHitCount = apiHitCount + 1
    print("  ")
    print("apiHitCount -------- ", apiHitCount)
    print("userIdsIndex,  dateListIndex", userIdsIndex, dateListIndex)
    isDateLast = False
    tempDateListIndex = dateListIndex + 1
    if dateListLen == tempDateListIndex:
        isDateLast = True
    if userIdsLen > userIdsIndex:
        if dateListLen > dateListIndex:
            status = login(userIds[userIdsIndex],
                           dateList[dateListIndex], isDateLast)
            if status == 3:
                # print("status cont... => ",
                #       userIds[userIdsIndex], dateList[dateListIndex])
                if isDateLast:
                    # print("not found id = ", userIds[userIdsIndex])
                    userIdsIndex = userIdsIndex + 1
                    dateListIndex = 0
                    return apiHit()
                else :
                    dateListIndex = dateListIndex + 1
                    return apiHit()
              
                # if dateListLen > dateListIndex:
                   
                # else:
                    
            elif status == 2:
                # print("worng id = ", userIds[userIdsIndex])
                userIdsIndex = userIdsIndex + 1
                dateListIndex = 0
                return apiHit()
            elif status == 1:
                print("found id = ",
                      userIds[userIdsIndex], dateList[dateListIndex])
                userIdsIndex = userIdsIndex + 1
                dateListIndex = 0
                return apiHit()
            else:
                print("something worng 1", userIdsIndex, dateListIndex)
        else:
            print("something worng 2")
            userIdsIndex = userIdsIndex + 1
            dateListIndex = 0
            return apiHit()
    else:
        print("work done")


def apiCall(id, date, isDateLast):
    status = 0
    print("   ")
    print("data =====", id, date, isDateLast)
    if id:
        print("   ")
    else:
         print("error =====", id, date, isDateLast)
    if isDateLast:
        print("============isDateLast true")
    if ((id == "123456") and (date == "17021986")):
        status = 1
    elif (id == "123457"):
        status = 2
    else:
        status = 3
    return status


startFn()
