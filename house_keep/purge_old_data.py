import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('YourTableName')
    today = 'YYYYMMDD'  # Replace with the actual date you want to delete

    response = table.scan(FilterExpression=Attr('date_column').begins_with(today))

    for item in response['Items']:
        table.delete_item(
            Key={
                'your_primary_key': item['your_primary_key']
            }
        )
