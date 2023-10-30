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


```
