import boto3
import json

def generate_items_json(table_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    
    response = table.scan()
    items = response['Items']
    
    # Continue scanning if there are more items
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        items.extend(response['Items'])
    
    # Convert items to JSON format
    json_data = json.dumps(items, indent=4)
    
    # Write JSON data to a file
    with open('items.json', 'w') as json_file:
        json_file.write(json_data)
    
    print("JSON file generated successfully.")

# Replace 'YourTableName' with the actual name of your DynamoDB table
generate_items_json('YourTableName')
