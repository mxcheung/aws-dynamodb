# Remove attribute from existing dynamodb table




Query the table:
```javascript

aws dynamodb scan \
  --table-name PetInventory \
```

# Results
```
{
    "Items": [
        {
            "insert_ts": {
                "S": "2023-10-21T12:34:56Z"
            },
            "pet_id": {
                "S": "124"
            },
            "pet_species": {
                "S": "Cat"
            }
        },
        {
            "insert_ts": {
                "S": "2021-10-21T12:34:56Z"
            },
            "pet_id": {
                "S": "125"
            },
            "pet_species": {
                "S": "Dog"
            }
        }
    ],
    "Count": 2,
    "ScannedCount": 2,
    "ConsumedCapacity": null
}
```


https://stackoverflow.com/questions/51660198/delete-all-items-in-a-dynamodb-table-using-bash-with-both-partition-and-sort-key

```
aws dynamodb describe-table --table-name $table_name | jq '.Table | del(.TableId, .TableArn, .ItemCount, .TableSizeBytes, .CreationDateTime, .TableStatus, .LatestStreamArn, .LatestStreamLabel, .ProvisionedThroughput.NumberOfDecreasesToday, .ProvisionedThroughput.LastIncreaseDateTime)' > schema.json

aws dynamodb delete-table --table-name $table_name

aws dynamodb create-table --cli-input-json file://schema.json
```
