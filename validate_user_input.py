import json

def lambda_handler(event, context):
    email = event.get('email')
    username = event.get('username')
    password = event.get('password')
    
    if not email or not username or not password:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid input')
        }
    
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
