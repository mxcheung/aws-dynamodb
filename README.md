# aws-dynamodb
aws dynamodb

## We are the littles
https://mydramalist.com/80113-we-are-the-littles


cd ~/environment/aws-dynamodb/


# Create table


To create the table using the AWS CLI, execute the following command in the Cloud9 terminal:

```
aws dynamodb create-table --cli-input-json file://~/environment/aws-dynamodb/aws-cli/dynamodb-table.json
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
aws dynamodb batch-write-item --request-items file://~/environment/aws-dynamodb/aws-cli/populate-dynamodb.json
```

Now, if you run the same command to scan all of the table contents, you'll find the items have been loaded into the table:

```
aws dynamodb scan --table-name LittlesTable
```


### Building A Docker Image

```
sudo yum -y install java-1.8.0-openjdk-devel
sudo alternatives --set java /usr/lib/jvm/java-1.8.0-openjdk.x86_64/bin/java
sudo alternatives --set javac /usr/lib/jvm/java-1.8.0-openjdk.x86_64/bin/javac

sudo wget http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo

sudo sed -i s/\$releasever/6/g /etc/yum.repos.d/epel-apache-maven.repo

sudo yum install -y apache-maven
```

```
cd ~/environment/aws-dynamodb/service
mvn clean install
```

aws sts get-caller-identity


cd ..
docker build . -t 123456789.dkr.ecr.ap-southeast-2.amazonaws.com/litles/service:latest

docker run -p 8080:8080 123456789.dkr.ecr.ap-southeast-2.amazonaws.com/litles/service:latest


https://f5c898c6e65144dd843332c102e79e82.vfs.cloud9.ap-southeast-2.amazonaws.com/swagger-ui/index.html?configUrl=/v3/api-docs/swagger-config

```
aws dynamodb update-table --table-name <YourTableName> --delete-protection-disabled
```


### Security


# This is a role which is used by the ECS tasks. Tasks in Amazon ECS define
  # the containers that should be deployed togehter and the resources they
  # require from a compute/memory perspective. So, the policies below will define
  # the IAM permissions that our Littles docker containers will have.
  ECSTaskRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Statement:
        - Effect: Allow
          Principal:
            Service: [ecs-tasks.amazonaws.com]
          Action: ['sts:AssumeRole']
      Path: /
      Policies:
        - PolicyName: AmazonECSTaskRolePolicy
          PolicyDocument:
            Statement:
            - Effect: Allow
              Action:
                # Allow the ECS Tasks to download images from ECR
                - 'ecr:GetAuthorizationToken'
                - 'ecr:BatchCheckLayerAvailability'
                - 'ecr:GetDownloadUrlForLayer'
                - 'ecr:BatchGetImage'

                # Allow the ECS tasks to upload logs to CloudWatch
                - 'logs:CreateLogStream'
                - 'logs:CreateLogGroup'
                - 'logs:PutLogEvents'
              Resource: '*'

            - Effect: Allow
              Action:
                # Allows the ECS tasks to interact with only the LittlesTable
                # in DynamoDB
                - 'dynamodb:Scan'
                - 'dynamodb:Query'
                - 'dynamodb:UpdateItem'
                - 'dynamodb:GetItem'
              Resource: 'arn:aws:dynamodb:*:*:table/LittlesTable*'

  
