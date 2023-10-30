# Remove attributes from existing items in table


# Step 1 create table

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


```
