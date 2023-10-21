from decimal import Decimal
import logging
from pprint import pprint

import boto3
from botocore.exceptions import ClientError
from datetime import datetime, timedelta
from boto3.dynamodb.conditions import Key, Attr

logger = logging.getLogger(__name__)

class PartiQLWrapper:
    """
    Encapsulates a DynamoDB resource to run PartiQL statements.
    """

    def __init__(self, dyn_resource):
        """
        :param dyn_resource: A Boto3 DynamoDB resource.
        """
        self.dyn_resource = dyn_resource


    def run_partiql(self, statement, params):
        """
        Runs a PartiQL statement. A Boto3 resource is used even though
        `execute_statement` is called on the underlying `client` object because the
        resource transforms input and output from plain old Python objects (POPOs) to
        the DynamoDB format. If you create the client directly, you must do these
        transforms yourself.

        :param statement: The PartiQL statement.
        :param params: The list of PartiQL parameters. These are applied to the
                       statement in the order they are listed.
        :return: The items returned from the statement, if any.
        """
        try:
            output = self.dyn_resource.meta.client.execute_statement(
                Statement=statement, Parameters=params
            )
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error(
                    "Couldn't execute PartiQL '%s' because the table does not exist.",
                    statement,
                )
            else:
                logger.error(
                    "Couldn't execute PartiQL '%s'. Here's why: %s: %s",
                    statement,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
        else:
            return output

title = "24 Hour PartiQL People"
year = datetime.now().year
    
dyn_res = boto3.resource("dynamodb")
wrapper = PartiQLWrapper(dyn_res)
output = wrapper.run_partiql(
    f'SELECT * FROM PetInventory', [title, year]
)
for item in output["Items"]:
    print(f"\n{item['pet_id']}, {item['insert_ts']}")
    pprint(output["Items"])
print("-" * 88)
