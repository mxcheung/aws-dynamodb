# python_remove_attribute.md

```
pip install boto

```


```
import boto3

# Create a Boto3 DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('PetInventory')

# Define the table name
table_name = 'PetInventory'

# Define the update expression to remove the "insert_ts" attribute
update_expression = "REMOVE insert_ts"

# Perform the scan operation and apply the update expression

# response = dynamodb.scan(
#    TableName=table_name,
#    UpdateExpression=update_expression
# )


response = table.update_item(
    Key={
        'pet_id': '124'
     },
    UpdateExpression="REMOVE insert_ts",
    ReturnValues="ALL_NEW"
)

# Print the response or handle it as needed
print(response)


def items(table) -> List[Dict]:
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
    update_expresssion = 'REMOVE attributeXyz'
    for item in old_references:
        logger.info('Remove attributeXyz attribute %s item with primary key.', item[primary_key])
        # table.update_item(Key={ primary_key: item[primary_key],  update_expresssion: update_expresssion  })
    logger.info('Done updating %s old settings.', len(old_references))
    return items


```
