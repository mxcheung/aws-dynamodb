# Rename attribute

# Step 1 fetch all records that contain attrib insert_ts

```
import boto3

# Create a Boto3 DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define the table name
table_name = 'PetInventory'

# Define the filter expression
filter_expression = 'attribute_exists(insert_ts)'

# Perform the scan operation with the filter expression
response = dynamodb.scan(
    TableName=table_name,
    FilterExpression=filter_expression
)

# Print the items that have the "insert_ts" attribute
items = response.get('Items', [])
for item in items:
    print(item)
```

# Step 2 rename all records that contain attrib insert_ts
