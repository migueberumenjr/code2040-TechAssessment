'''
Author: Miguel Angel Berumen Jr
Email: maberume@ucsc.edu
2nd email: migueberumenjr@gmail.com
Purpose: Code2040 Technical Assessment for the 2017 Fellows
'''
#These modules are required for each step in the challenge
import json
import requests
import datetime
import iso8601

'''
This function is for Step 1
It registers me for the challenge using my unique token and github repository
It returns my token for use in the following functions
'''
def stage1():
    #My unique token
    token = "a8b4348a10cd839fd0556ed099107e96"
    
    #Create a dicionary with my token and github repo
    regObj = {"token": token,"github": "https://github.com/migueberumenjr/code2040-TechAssessment/blob/migueberumenjr-step1-1/"}
    
    #POST my dictionary to the registration endpoint and register
    regAPI = requests.post("http://challenge.code2040.org/api/register", json=regObj)
    print(regAPI.text)
    return token

'''
This function is for Step 2
It reverses a given string
'''
def stage2(token):
    #Dictionary for my token
    tokDic = {"token": token}
    
    #Get the string
    strRes = requests.post("http://challenge.code2040.org/api/reverse", json=tokDic)
    #print(strRes.text)
    strText = strRes.text
    
    #Reverse the string
    revStr = strText[::-1]
    #print(revStr)

    #POST the reversed string
    strDic = {"token": token, "string": revStr}
    strVal = requests.post("http://challenge.code2040.org/api/reverse/validate", json=strDic)
    print(strVal.text)

'''
This function is for Step 3
It finds a string in a list of strings 
and returns the position of the given string in that list
'''
def stage3(token):
    tokDic = {"token": token}
    
    #Get the needle/haystack dictionary
    needRes = requests.post("http://challenge.code2040.org/api/haystack", json=tokDic)
    hayDic = json.loads(needRes.text)
    
    #Get the haystack list
    haystack = hayDic["haystack"]

    #Find the needle string in the haystack list and return the position
    for index in range(len(haystack)):
        if hayDic["needle"] == haystack[index]:
            needle = index
            break;
    
    #POST the position of the needle string
    needDic = {"token": token, "needle": needle}
    needVal = requests.post("http://challenge.code2040.org/api/haystack/validate", json=needDic)
    print(needVal.text)

'''
This function is for Step 4
It returns a list of strings that do not contain the given prefix
'''
def stage4(token):
    tokDic = {"token": token}
    
    #Get the prefix and string list dictionary
    preRes = requests.post("http://challenge.code2040.org/api/prefix", json=tokDic)
    preDic = json.loads(preRes.text)

    #Get the list of strings to loop through
    strings = preDic["array"]
    #print(strings)
    #print(preDic["prefix"])
    preArray = []

    #Find all the strings that do not contain the prefix
    #Append those strings to a list
    for word in strings:
        if preDic["prefix"] not in word:
            preArray.append(word)

    #print(preArray)
    #POST the list 
    wordsDic = {"token": token, "array": preArray}
    preVal = requests.post("http://challenge.code2040.org/api/prefix/validate", json=wordsDic)
    print(preVal.text)
    
'''
This function is for Step 5
It adds time to a datestamp/datetime instance
'''
def stage5(token):
    tokDic = {"token": token}
    
    #Get the datestamp and the seconds to add
    dateRes = requests.post("http://challenge.code2040.org/api/dating", json=tokDic)
    dateDic = json.loads(dateRes.text)

    #Convert the datestamp and seconds for usage
    date = str(dateDic["datestamp"])
    seconds = str(dateDic["interval"])
    intConv = datetime.timedelta(seconds=int(seconds))
    #print(date)
    #print(seconds)
    #print(intConv)

    #Add seconds to datestamp
    parseDate = iso8601.parse_date(date)
    updateTime = parseDate + intConv
    #print(parseDate)
    #print(updateTime)

    #Convert datestamp back to format given
    dateUpdate = updateTime.strftime("%Y-%m-%dT%H:%M:%SZ")
    #print(dateUpdate)

    #POST new datestamp
    newDateDic = {"token": token, "datestamp": dateUpdate}
    dateVal = requests.post("http://challenge.code2040.org/api/dating/validate", json=newDateDic)
    print(dateVal.text)

'''
This is the main function
It calls each function for each step
'''
def main():
    token = stage1()
    stage2(token)
    stage3(token)
    stage4(token)
    stage5(token)

#This calls the main function
main()
