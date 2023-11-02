import boto3
from typing import Dict, List

# Create a Boto3 DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('PetInventory')

# Define the table name
table_name = 'PetInventory'


def get_items(table) -> List[Dict]:
    # Define the filter expression for scanning

    # Define the expression attribute values
    expression_attribute_values = {
        ':species_value': 'Dog'
    }
    
    # Define the filter expression
    filter_expression = 'pet_species = :species_value'

    response = table.scan( FilterExpression=filter_expression,
                           ExpressionAttributeValues=expression_attribute_values )
    records = response['Items'] if 'Items' in response else []
    while response.get('LastEvaluatedKey'):
        start_key = response['LastEvaluatedKey']
        response = table.scan(
            ExclusiveStartKey=start_key
        )
        records.extend(response['Items'])
    return records

def get_items_with_insert_ts(table) -> List[Dict]:
    # Define the filter expression
    filter_expression = 'attribute_exists(insert_ts)'
    response = table.scan( FilterExpression=filter_expression )
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
    for item in old_references:
        if 'insert_ts' in item:
             # Rename the attribute and remove the original one
             table.update_item(Key={ primary_key: item[primary_key]},  
                               UpdateExpression= update_expression)
             print("hello")
    return items


response = get_items(table)
remove_attribute_references(response,'pet_id', table) 
