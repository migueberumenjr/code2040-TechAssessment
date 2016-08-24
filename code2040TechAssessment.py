import requests
import json

def reg():
  '''
	This function will POST my JSON object to the registration endpoint for the API challenge
	'''
	regObj = {"token": "a8b4348a10cd839fd0556ed099107e96","github": "https://github.com/migueberumenjr/code2040-TechAssessment/tree/migueberumenjr-step1-1"}
	regAPI = requests.post("http://challenge.code2040.org/api/register", data=json.dumps(regObj))
  
  return true
