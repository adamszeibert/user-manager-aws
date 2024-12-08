import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    email = event['pathParameters']['email']
    
    table.delete_item(Key={'email': email})
    
    return {
        'statusCode': 200,
        'body': json.dumps('User deleted')
    }