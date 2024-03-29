# Create a DynamoDB Table Using the AWS CLI

Enter the following create-table command in the terminal:

```python
aws dynamodb\
    create-table\
        --table-name PetInventory\
        --attribute-definitions\
            AttributeName=pet_species,AttributeType=S\
            AttributeName=pet_id,AttributeType=N\
        --key-schema\
            AttributeName=pet_species,KeyType=HASH\
            AttributeName=pet_id,KeyType=RANGE\
        --billing-mode PAY_PER_REQUEST

aws dynamodb\
    create-table\
        --table-name PetInventory\
        --attribute-definitions\
            AttributeName=pet_species,AttributeType=S\
            AttributeName=pet_id,AttributeType=N\
            AttributeName=insert_ts,AttributeType=S\
        --key-schema\
            AttributeName=pet_species,KeyType=HASH\
            AttributeName=pet_id,KeyType=RANGE\

aws dynamodb\
    create-table\
        --table-name PetInventory\
        --attribute-definitions\
            AttributeName=pet_id,AttributeType=S\
        --key-schema\
            AttributeName=pet_id,KeyType=HASH\
        --billing-mode PAY_PER_REQUEST   --billing-mode PAY_PER_REQUEST

```


Check the table was created:
```javascript
aws dynamodb describe-table --table-name PetInventory
```

Syntax for inserting a record:
```javascript
aws dynamodb put-item --table-name TableName --item '{
    "AttributeName1": {"DataType": "AttributeType1", "AttributeValue": "Value1"},
    "AttributeName2": {"DataType": "AttributeType2", "AttributeValue": "Value2"},
    ...
}'

aws dynamodb put-item --table-name MyTable --item '{
    "ID": {"S": "123"},
    "Timestamp": {"N": "1634850000"},
    "Name": {"S": "SampleName"},
    "Value": {"N": "42"},
    "insert_ts": {"S": "2023-10-21T12:34:56Z"}
}'

aws dynamodb put-item --table-name PetInventory --item '{
    "pet_id": {"N": "123"},
    "pet_species": {"S": "Cat"}
}'


aws dynamodb put-item --table-name PetInventory --item '{
    "pet_id": {"S": "124"},
    "pet_species": {"S": "Cat"},
   "insert_ts": {"S": "2023-10-21T12:34:56Z"}
}'


aws dynamodb put-item --table-name PetInventory --item '{
    "pet_id": {"S": "125"},
    "pet_species": {"S": "Dog"},
   "insert_ts": {"S": "2021-10-21T12:34:56Z"}
}'


```

Query the table:
```javascript
aws dynamodb scan \
  --table-name YourTableName \
  --filter-expression "insert_ts <= :oneYearAgo" \
  --expression-attribute-values '{":oneYearAgo": {"S": "YYYY-MM-DDTHH:MM:SSZ"}}'

aws dynamodb scan \
  --table-name PetInventory \
  --filter-expression "insert_ts <= :oneYearAgo" \
  --expression-attribute-values '{":oneYearAgo": {"S": "2022-12-21T12:34:56Z"}}'

```

Delete the table:
```javascript
aws dynamodb delete-table --table-name PetInventory
```

Here's an example in Python using the Boto3 library:
```python
import boto3
import json

dynamodb = boto3.client('dynamodb')
table_name = 'YourTableName'

response = dynamodb.scan(TableName=table_name)

items = response['Items']
json_data = json.dumps(items, indent=2)
with open('exported_data.json', 'w') as outfile:
    outfile.write(json_data)
```

Execute the Query: Use the AWS SDK to execute the PartiQL query against your DynamoDB table.

Here's an example of executing the query using Python and the Boto3 library:
```python
import boto3

dynamodb = boto3.client('dynamodb')

query = "DELETE FROM YourTableName WHERE #timestamp < :one_year_ago"
query_params = {
    "#timestamp": "timestamp",
    ":one_year_ago": {"S": "2022-10-21T00:00:00Z"}  # Replace with the actual timestamp one year ago
}

response = dynamodb.execute_statement(Statement=query, Parameters=query_params)

```

```python
import boto3

dynamodb = boto3.client('dynamodb')

query = "DELETE FROM PetInventory WHERE #timestamp < :one_year_ago"
query_params = {
    "#timestamp": "insert_ts",
    ":one_year_ago": {"S": "2022-10-21T00:00:00Z"}  # Replace with the actual timestamp one year ago
}

response = dynamodb.execute_statement(Statement=query, Parameters=query_params)

```






```python
import boto3
from datetime import datetime, timedelta
from boto3.dynamodb.conditions import Key, Attr

# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('PetInventory')

# Calculate the date one year ago from the current date
one_year_ago = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')

# Perform a scan to identify items to delete


response = table.scan(
        FilterExpression=Attr('insert_ts').lt(one_year_ago)
    )

# Extract the items to be deleted
items_to_delete = response.get('Items', [])

# Delete the items in batches (25 items per batch)
with table.batch_writer() as batch:
    for item in items_to_delete:
        batch.delete_item(
            Key={
                'pet_id': item['pet_id']
            }
        )

print(f"Deleted {len(items_to_delete)} items.")

```
