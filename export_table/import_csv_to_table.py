import csv
import boto3

# Initialize Boto3 DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='your_region_name')

# Specify the name of the DynamoDB table
table_name = 'your_table_name'

# Open the CSV file
with open('your_csv_file.csv', 'r') as csvfile:
    # Parse the CSV file
    csvreader = csv.DictReader(csvfile)
    
    # Access the DynamoDB table
    table = dynamodb.Table(table_name)
    
    # Iterate through each row in the CSV file
    for row in csvreader:
        # Extract data from the row
        item = {}
        for key, value in row.items():
            # Dynamically convert data types if needed
            # For example, convert strings to integers or floats
            item[key] = value
        
        # Load the item into the DynamoDB table
        table.put_item(Item=item)
        
print("CSV data loaded into DynamoDB table successfully!")
