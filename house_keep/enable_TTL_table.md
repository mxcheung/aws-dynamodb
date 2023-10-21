# Create a DynamoDB Table Using the AWS CLI

able TTL on the TTLExample table.

```python
aws dynamodb update-time-to-live --table-name TTLExample --time-to-live-specification "Enabled=true, AttributeName=ttl"
```


escribe TTL on the TTLExample table.
```javascript
aws dynamodb describe-time-to-live --table-name TTLExample
{
    "TimeToLiveDescription": {
        "AttributeName": "ttl",
        "TimeToLiveStatus": "ENABLED"
    }
} 
```

Add an item to the TTLExample table with the Time to Live attribute set using the BASH shell and the AWS CLI.
```javascript


EXP=`date -d '+5 days' +%s`
aws dynamodb put-item --table-name "TTLExample" --item '{"id": {"N": "1"}, "ttl": {"N": "'$EXP'"}}'


```
