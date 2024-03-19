import json
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('visitorcount')

def increment_visitor_count():
    table.update_item(
        Key={ 'WebPropertyName': 'VisitorCount' },
        UpdateExpression='ADD VisitorCount :n',
        ExpressionAttributeValues={
            ':n': 1
        }
    )

def get_visitor_count():
    # if not exist, create
    res = table.get_item(
        Key={ 'WebPropertyName': 'VisitorCount'}
    )
    if 'Item' not in res:
        table.put_item(
            Item={ 'WebPropertyName': 'VisitorCount', 'VisitorCount': 0 }
        )
        return 0
    
    return int(res['Item']['VisitorCount'])
    
def lambda_handler(event, context):
    if 'queryStringParameters' not in event:
        return {
            'statusCode': 400,
            'headers': {
              'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps('error: action not supplied')
        }
    if 'action' not in event['queryStringParameters']:
        return {
            'statusCode': 400,
            'headers': {
              'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps('error: action not supplied')
        }
        
    action = event['queryStringParameters']['action']
    count = get_visitor_count()
    match action:
        case 'increment':
            increment_visitor_count()
            return {
                'statusCode': 200,
                'headers': {
                  'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps(count + 1)
            }
        case 'get':
            return {
                'statusCode': 200,
                'headers': {
                  'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps(count)
            }
        case _:
            return {
                'statusCode': 400,
                'headers': {
                  'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps('error: unknown action')
            }