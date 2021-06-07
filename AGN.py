# WORKING-GREEN
import codecs
import csv
import datetime
import boto3
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
# from cryptography.fernet import Fernet

from boto3.dynamodb.conditions import Key, Attr

def data_entry():
    dynamodb = boto3.resource('dynamodb', aws_access_key_id="access_id",aws_secret_access_key="secret_access_id")
    
    value = {}
    for x in range(5):
        value["Que" + str(x)] = "Ans" + str(x)
    print(value)
    curr_timestamp=str(datetime.datetime.now())
    table = dynamodb.Table('agn_details')
    count = 1
    for x in range(10):
        agn_id = "agn1" + str(count)
        count += 1
        table.put_item(
            Item={
                'agn_id': agn_id,
                'info': value,
                'created_timestamp':curr_timestamp,  
                'updated_timestamp':curr_timestamp,
                'current_status': 'Created by Aetna User',
                'is_deleted':False                
            }
        )
#lambda_function.py
#Displaying lambda_function.py.
data_entry()