package com.example.little.service;

import java.util.HashMap;
import java.util.List;

import org.springframework.stereotype.Service;

import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClientBuilder;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBMapper;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBQueryExpression;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBScanExpression;
import com.amazonaws.services.dynamodbv2.model.AttributeValue;
import com.example.little.model.Little;
import com.example.little.model.Littles;

@Service
public class LittlesService {

    private final AmazonDynamoDB client = AmazonDynamoDBClientBuilder.defaultClient();
    private DynamoDBMapper mapper = new DynamoDBMapper(client);

    public Littles getAllLittles() {

        List<Little> Littles = mapper.scan(Little.class, new DynamoDBScanExpression());
        Littles allLittles = new Littles(Littles);

        return allLittles;
    }

    public Littles queryLittleItems(String filter, String value) {

        HashMap<String, AttributeValue> attribValue = new HashMap<String, AttributeValue>();
        attribValue.put(":"+value,  new AttributeValue().withS(value));

        DynamoDBQueryExpression<Little> queryExpression = new DynamoDBQueryExpression<Little>()
                .withIndexName(filter+"Index")
                .withKeyConditionExpression(filter + "= :" + value)
                .withExpressionAttributeValues(attribValue)
                .withConsistentRead(false);

        List<Little> Littles = mapper.query(Little.class, queryExpression);
        Littles allLittles = new Littles(Littles);

        return allLittles;
    }

}
