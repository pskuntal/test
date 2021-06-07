import json
import requests


def lambda_handler(event, context):
    response = requests.get('https://w3schools.com')
    # response.status_code
    #print(response.json())
    return response.json()

