import boto3
from db import save_to_dynamodb

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Get VPCs
    vpcs = ec2.describe_vpcs().get('Vpcs', [])
    
    # Get Subnets
    subnets = ec2.describe_subnets().get('Subnets', [])
    
    data = {
        "vpcs": vpcs,
        "subnets": subnets
    }

    # Save to DB
    save_to_dynamodb(data)

    return {
        'statusCode': 200,
        'body': 'VPCs and Subnets saved successfully!'
    }
