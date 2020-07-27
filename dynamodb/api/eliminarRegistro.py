import os
import boto3
import botocore
from utils.responseUtils import ResponseUtils


def handler(event, context):
    dynamo = boto3.client("dynamodb")
    try:
        response = dynamo.delete_item(
            Key={
                'ID': {
                    'S': '',  # ID de registro en la tabla
                }
            },
            TableName=os.environ["TABLE_NAME"],
        )
        print(response)
        return ResponseUtils.success(200, "Registro eliminado con exito")
    except botocore.exceptions.ClientError as e:
        print(e.response)
        if e.response["Error"]["Code"] == "ValidationException":
            return ResponseUtils.error(500, e.response["Error"]["Message"])
