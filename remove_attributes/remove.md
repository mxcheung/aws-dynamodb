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
