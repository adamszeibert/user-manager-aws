import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    email = event['pathParameters']['email']
    
    response = table.get_item(Key={'email': email})
    
    if 'Item' not in response:
        return {
            'statusCode': 404,
            'body': json.dumps('User not found')
        }
    
    return {
        'statusCode': 200,
        'body': json.dumps(response['Item'])
    }