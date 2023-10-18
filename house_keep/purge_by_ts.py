import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('YourTableName')
    
    # Calculate the date one year ago from the current date
    one_year_ago = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')

    response = table.scan(
        FilterExpression=Attr('timestamp_column').lt(one_year_ago)
    )

    for item in response['Items']:
        table.delete_item(
            Key={
                'your_primary_key': item['your_primary_key']
            }
        )
