import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    email = body.get('email')
    
    response = table.get_item(Key={'email': email})
    
    if 'Item' in response:
        return {
            'statusCode': 400,
            'body': json.dumps('User already exists')
        }
    
    return {
        'statusCode': 200,
        'body': json.dumps(body)
    }