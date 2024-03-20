import json
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('visitorcount')

ERROR = {
    'statusCode': 400,
    'headers': {
        'Access-Control-Allow-Origin': '*'
    }
}

OK = {
    'statusCode': 200,
    'headers': {
        'Access-Control-Allow-Origin': '*'
    },
}

def increment_visitor_count():
    table.update_item(
        Key={ 'WebPropertyName': 'VisitorCount' },
        UpdateExpression='ADD VisitorCount :n',
        ExpressionAttributeValues={
            ':n': 1
        }
    )

def get_visitor_count():
    # get visitor count from the table
    res = table.get_item(
        Key={ 'WebPropertyName': 'VisitorCount'}
    )

    # if not exist, create entry
    if 'Item' not in res:
        table.put_item(
            Item={ 'WebPropertyName': 'VisitorCount', 'VisitorCount': 0 }
        )
        return 0
    
    return int(res['Item']['VisitorCount'])
    
def lambda_handler(event, context):
    # query parameters should automatically be verified by SAM api

    action = event['queryStringParameters']['action']
    count = get_visitor_count()
    match action:
        case 'increment':
            increment_visitor_count()
            return {
                **OK,
                'body': json.dumps(count + 1)
            }
        case 'get':
            return {
                **OK,
                'body': json.dumps(count)
            }
        case _:
            return {
                **ERROR,
                'body': json.dumps('error: unknown action')
            }