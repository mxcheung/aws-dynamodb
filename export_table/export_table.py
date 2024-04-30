import boto3
import json

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb')

# Name of the DynamoDB table
table_name = 'YourDynamoDBTableName'

# Function to scan the DynamoDB table and return all items
def scan_table():
    response = dynamodb.scan(TableName=table_name)
    return response['Items']

# Function to save the items to a JSON file
def save_to_json(items):
    with open('items.json', 'w') as json_file:
        json.dump(items, json_file, indent=4)

if __name__ == '__main__':
    items = scan_table()
    save_to_json(items)
    print('Items saved to items.json')
