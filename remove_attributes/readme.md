# Remove attributes from existing items in table


# Step 1 create table

# Create a DynamoDB Table Using the AWS CLI

Enter the following create-table command in the terminal:

```python

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
  --table-name PetInventory \
```


Delete the table:
```javascript
aws dynamodb delete-table --table-name PetInventory
```
