import boto3
from typing import Dict, List

# Create a Boto3 DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('PetInventory')

# Define the table name
table_name = 'PetInventory'


def get_items(table) -> List[Dict]:
    response = table.scan()
    records = response['Items'] if 'Items' in response else []
    while response.get('LastEvaluatedKey'):
        start_key = response['LastEvaluatedKey']
        response = table.scan(
            ExclusiveStartKey=start_key
        )
        records.extend(response['Items'])
    return records

def remove_attribute_references(old_references, primary_key, table):
    items = len(old_references)
    # Define the update expression to rename "insert_ts" to "insert_timestamp"
    update_expression = "SET insert_timestamp = insert_ts REMOVE insert_ts"
    conditional_expression = "attribute_exists(insert_ts)"
    for item in old_references:
        if 'insert_ts' in item:
             # Rename the attribute and remove the original one
             table.update_item(Key={ "pet_id": item[primary_key]},  
                               UpdateExpression= update_expression,  
                               ConditionExpression=conditional_expression
                               )
             print("hello")
    return items


response = get_items(table)
remove_attribute_references(response,'pet_id', table) 
