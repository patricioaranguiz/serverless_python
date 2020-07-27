import boto3
import botocore
import os
from utils.responseUtils import ResponseUtils


def handler(event, context):
    dynamo = boto3.client("dynamodb")
    try:

        response = dynamo.query(
            ExpressionAttributeValues={
                ':id': {
                    'S': '',  # ID de registro en la tabla
                },
            },
            KeyConditionExpression='ID = :id',
            ProjectionExpression='Nombre, Anno',
            TableName=os.environ["TABLE_NAME"],
        )

        print(response.get("Items"))
        return ResponseUtils.success(200, response.get("Items"))
    except botocore.exceptions.ClientError as e:
        print(e.response["Error"]["Code"])
        return ResponseUtils.error(500, e.response["Error"]["Message"])
