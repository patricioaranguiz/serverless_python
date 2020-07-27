import boto3
import botocore
import os
from utils.responseUtils import ResponseUtils


def handler(event, context):
    dynamo = boto3.client("dynamodb")
    try:
        response = dynamo.scan(
            ExpressionAttributeNames={
                '#A': 'Anno',
                '#N': 'Nombre',
            },
            ExpressionAttributeValues={
                ':a': {
                    'S': '',  # ID de registro en la tabla
                },
            },
            FilterExpression='ID = :a',
            ProjectionExpression='#N, #A',
            TableName=os.environ["TABLE_NAME"],
        )

        print(response.get("Items"))
        return ResponseUtils.success(200, response.get("Items"))

    except botocore.exceptions.ClientError as e:
        print(e.response)
        return ResponseUtils.error(500, e.response["Error"]["Message"])
