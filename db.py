import boto3
import uuid
import json

def save_to_dynamodb(data):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('VPCData')  # Ensure table exists

    item = {
        "id": str(uuid.uuid4()),
        "data": json.dumps(data)
    }

    table.put_item(Item=item)
