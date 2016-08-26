import json
import requests

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

    print(strRes.text)
    strText = strRes.text
    revStr = strText[::-1]
    print(revStr)

    strDic = {"token": token, "string": revStr}
    strVal = requests.post("http://challenge.code2040.org/api/reverse/validate", json=strDic)
    print(strVal.text)

def main():
    token = stage1()
    stage2(token)

main()
