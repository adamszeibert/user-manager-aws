import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    email = event.get('email')
    username = event.get('username')
    password = event.get('password')
    
    table.update_item(
        Key={'email': email},
        UpdateExpression='SET username = :username, password = :password',
        ExpressionAttributeValues={':username': username, ':password': password}
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('User updated')
    }