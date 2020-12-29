# aws-dynamodb
aws dynamodb




# Create table


To create the table using the AWS CLI, execute the following command in the Cloud9 terminal:

```
aws dynamodb create-table --cli-input-json file://~/environment/aws-modern-application-workshop/module-3/aws-cli/dynamodb-table.json
```

After the command runs, you can view the details of your newly created table by executing the following AWS CLI command in the terminal:

```
aws dynamodb describe-table --table-name LittlesTable
```


If we execute the following command to retrieve all of the items stored in the table, you'll see that the table is empty:

```
aws dynamodb scan --table-name LittlesTable
```

```
{
    "Count": 0,
    "Items": [],
    "ScannedCount": 0,
    "ConsumedCapacity": null
}
```


### Add Items to the DynamoDB Table

Also provided is a JSON file that can be used to batch insert a number of Little items into this table.  This will be accomplished through the DynamoDB API **BatchWriteItem.** To call this API using the provided JSON file, execute the following terminal command (the response from the service should report that there are no items that went unprocessed):

```
aws dynamodb batch-write-item --request-items file://~/environment/aws-modern-application-workshop/module-3/aws-cli/populate-dynamodb.json
```

Now, if you run the same command to scan all of the table contents, you'll find the items have been loaded into the table:

```
aws dynamodb scan --table-name LittlesTable
```