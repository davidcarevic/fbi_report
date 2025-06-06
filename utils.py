import requests
import phonenumbers
import json
from phonenumbers.phonenumberutil import NumberParseException
from pprint import pprint

def getCase(query):
    url = "https://api.fbi.gov/wanted/v1/list"
    response = requests.get(url, params={"title": query})
    if response.status_code == 200:
        data = response.json()
        return data
    return False

def checkPhone(phone):
    try:
        parsed = phonenumbers.parse(phone, None)
        isValid = phonenumbers.is_valid_number(parsed)
        region = 'Unknown'
        if isValid:
            try:
                region = phonenumbers.region_code_for_number(parsed)
            except:
                pass

        phoneData = {
            'valid': isValid,
            'region': region
        }
        return phoneData
    except NumberParseException:
        return {
            'valid': False,
            'region': 'Unknown'
        }
    
def getClientIP():
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=5)
        if response.status_code == 200:
            return response.json().get('ip', 'Unavailable')
    except requests.RequestException as e:
        print("Error:", e)

    return 'Unavailable'

def saveReport(report, filename='reports.json'):
    try:
        with open(filename, 'r') as f:
            existing = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        existing = []

    existing.append(report)

    with open(filename, 'w') as f:
        json.dump(existing, f, indent=2)
