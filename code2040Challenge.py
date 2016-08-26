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

def main():
    stage1()

main()
