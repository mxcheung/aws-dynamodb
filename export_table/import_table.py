import boto3
import json

def load_items_to_table(table_name, json_file_path):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    
    with open(json_file_path) as json_file:
        items = json.load(json_file)
    
    with table.batch_writer() as batch:
        for item in items:
            batch.put_item(Item=item)
    
    print("Data loaded into DynamoDB table successfully.")

# Replace 'YourTableName' with the actual name of your DynamoDB table
# Replace 'items.json' with the actual path to your JSON file
load_items_to_table('YourTableName', 'items.json')
