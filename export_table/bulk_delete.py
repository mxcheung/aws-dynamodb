import boto3

def batch_delete_items(table_name, keys):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    
    with table.batch_writer() as batch:
        for key in keys:
            batch.delete_item(Key=key)

if __name__ == "__main__":
    # Define the table name
    table_name = 'YourDynamoDBTableName'
    
    # Define the list of keys to delete
    # Example: [{'PrimaryKey': 'Value1'}, {'PrimaryKey': 'Value2'}]
    keys = [
        {'PrimaryKey': 'Value1'},
        {'PrimaryKey': 'Value2'},
        # Add more keys as needed
    ]
    
    # Call the function to delete items
    batch_delete_items(table_name, keys)
