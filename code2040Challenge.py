import json
import requests
import datetime
import iso8601

def stage1():
    '''
    This script will POST my JSON object to the registration endpoint for the API challenge
    '''
    token = "a8b4348a10cd839fd0556ed099107e96"
    regObj = {"token": token,"github": "https://github.com/migueberumenjr/code2040-TechAssessment/blob/migueberumenjr-step1-1/"}
    regAPI = requests.post("http://challenge.code2040.org/api/register", json=regObj)
    print(regAPI.text)
    return token

def stage2(token):
    tokDic = {"token": token}
    strRes = requests.post("http://challenge.code2040.org/api/reverse", json=tokDic)

    #print(strRes.text)
    strText = strRes.text
    revStr = strText[::-1]
    #print(revStr)

    strDic = {"token": token, "string": revStr}
    strVal = requests.post("http://challenge.code2040.org/api/reverse/validate", json=strDic)
    print(strVal.text)

def stage3(token):
    tokDic = {"token": token}
    needRes = requests.post("http://challenge.code2040.org/api/haystack", json=tokDic)
    hayDic = json.loads(needRes.text)
    
    haystack = hayDic["haystack"]

    for index in range(len(haystack)):
        if hayDic["needle"] == haystack[index]:
            needle = index
            break;
    needDic = {"token": token, "needle": needle}
    needVal = requests.post("http://challenge.code2040.org/api/haystack/validate", json=needDic)
    print(needVal.text)

def stage4(token):
    tokDic = {"token": token}
    preRes = requests.post("http://challenge.code2040.org/api/prefix", json=tokDic)
    preDic = json.loads(preRes.text)

    strings = preDic["array"]
    #print(strings)
    #print(preDic["prefix"])
    preArray = []

    for word in strings:
        if preDic["prefix"] not in word:
            preArray.append(word)

    #print(preArray)
    wordsDic = {"token": token, "array": preArray}
    preVal = requests.post("http://challenge.code2040.org/api/prefix/validate", json=wordsDic)
    print(preVal.text)

def stage5(token):
    tokDic = {"token": token}
    dateRes = requests.post("http://challenge.code2040.org/api/dating", json=tokDic)
    dateDic = json.loads(dateRes.text)

    date = str(dateDic["datestamp"])
    seconds = str(dateDic["interval"])
    intConv = datetime.timedelta(seconds=int(seconds))
    #print(date)
    #print(seconds)
    #print(intConv)

    parseDate = iso8601.parse_date(date)
    updateTime = parseDate + intConv
    #print(parseDate)
    #print(updateTime)

    dateUpdate = updateTime.strftime("%Y-%m-%dT%H:%M:%SZ")
    #print(dateUpdate)

    newDateDic = {"token": token, "datestamp": dateUpdate}
    dateVal = requests.post("http://challenge.code2040.org/api/dating/validate", json=newDateDic)
    print(dateVal.text)
    
def main():
    token = stage1()
    stage2(token)
    stage3(token)
    stage4(token)
    stage5(token)

main()
