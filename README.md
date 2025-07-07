# AWS Lambda – VPC & Subnet Exporter

This AWS Lambda function lists all VPCs and Subnets in the current account and stores the data in a DynamoDB table.

## 🛠 Requirements

- AWS Account
- IAM Role with `ec2:DescribeVpcs`, `ec2:DescribeSubnets`, and `dynamodb:PutItem` permissions
- Python 3.8+
- DynamoDB table named `VPCData`

## 🚀 Deployment

1. Zip and upload via AWS Lambda Console or AWS CLI:
```bash
zip function.zip lambda_function.py db.py
