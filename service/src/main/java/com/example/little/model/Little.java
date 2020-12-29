package com.example.little.model;

import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBAttribute;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBHashKey;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBTable;

@DynamoDBTable(tableName = "LittlesTable")
public class Little {

    private String littleId;
    private String name;
    private Integer age;
    private String description;

    public Little() {
    }

    @DynamoDBHashKey(attributeName = "LittleId")
    public String getLittlesId() {
        return littleId;
    }

    public void setLittlesId(String littleId) {
        this.littleId = littleId;
    }

    @DynamoDBAttribute(attributeName = "Name")
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @DynamoDBAttribute(attributeName = "Age")
    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

    @DynamoDBAttribute(attributeName = "Description")
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

}
