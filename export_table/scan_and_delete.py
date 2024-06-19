import boto3

def delete_all_items(table_name):
    # Initialize a session using Amazon DynamoDB
    session = boto3.Session()
    dynamodb = session.resource('dynamodb')
    
    # Select your DynamoDB table
    table = dynamodb.Table(table_name)
    
    # Scan the table and delete each item
    scan = table.scan()
    with table.batch_writer() as batch:
        for each in scan['Items']:
            batch.delete_item(
                Key={
                    'PrimaryKeyAttributeName': each['PrimaryKeyAttributeName'],  # Replace with your table's primary key attribute name
                    # 'SortKeyAttributeName': each['SortKeyAttributeName']  # If you have a sort key, uncomment and replace
                }
            )
    
    while 'LastEvaluatedKey' in scan:
        scan = table.scan(ExclusiveStartKey=scan['LastEvaluatedKey'])
        with table.batch_writer() as batch:
            for each in scan['Items']:
                batch.delete_item(
                    Key={
                        'PrimaryKeyAttributeName': each['PrimaryKeyAttributeName'],  # Replace with your table's primary key attribute name
                        # 'SortKeyAttributeName': each['SortKeyAttributeName']  # If you have a sort key, uncomment and replace
                    }
                )

if __name__ == "__main__":
    table_name = 'YourTableName'  # Replace with your DynamoDB table name
    delete_all_items(table_name)
    print(f"All items from table '{table_name}' have been deleted.")
