import boto3

# Initialize a DynamoDB client
dynamodb = boto3.client('dynamodb', region_name='your_region')

# Define the table name
table_name = 'YourTableName'

# Define the Cloud9 key attribute name
cloud9_key_attribute_name = 'Cloud9Key'

# Define the timestamp attribute name
timestamp_attribute_name = 'Timestamp'

# Define the primary key schema
key_schema = [
    {
        'AttributeName': cloud9_key_attribute_name,
        'KeyType': 'HASH'  # Partition key
    },
    {
        'AttributeName': timestamp_attribute_name,
        'KeyType': 'RANGE'  # Sort key
    }
]

# Define the attribute definitions
attribute_definitions = [
    {
        'AttributeName': cloud9_key_attribute_name,
        'AttributeType': 'S'  # String
    },
    {
        'AttributeName': timestamp_attribute_name,
        'AttributeType': 'N'  # Number
    }
]

# Provisioned throughput settings (you can adjust these as needed)
read_capacity_units = 5
write_capacity_units = 5

# Create the DynamoDB table
response = dynamodb.create_table(
    TableName=table_name,
    KeySchema=key_schema,
    AttributeDefinitions=attribute_definitions,
    ProvisionedThroughput={
        'ReadCapacityUnits': read_capacity_units,
        'WriteCapacityUnits': write_capacity_units,
    }
)

# Wait for the table to be created (this can take a few minutes)
table_waiter = dynamodb.get_waiter('table_exists')
table_waiter.wait(TableName=table_name)

print(f"Table '{table_name}' has been created.")














===============================================================================================================

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

===============================================================================================================


import boto3
ddb = boto3.client('dynamodb')
createResponse = ddb.create_table(
    AttributeDefinitions=[
        {
            'AttributeName':'pet_species',
            'AttributeType': 'S',
        }, 
        {
            'AttributeName':'pet_id',
            'AttributeType':'N'
        }
    ], 
    KeySchema=[
        {
            'AttributeName':'pet_species',
            'KeyType':'HASH'
        },
        {
            'AttributeName':'pet_id',
            'KeyType':'RANGE'
        },
    ],
    BillingMode = 'PAY_PER_REQUEST',
    TableName='PetInventory'
)


===============================================================================================================              

            
