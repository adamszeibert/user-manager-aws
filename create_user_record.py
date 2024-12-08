import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    email = body.get('email')
    username = body.get('username')
    password = body.get('password')
    
    table.put_item(Item={'email': email, 'username': username, 'password': password})
    
    return {
        'statusCode': 200,
        'body': json.dumps('User created')
    }