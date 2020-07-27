import boto3
import botocore
import os
from utils.responseUtils import ResponseUtils


def handler(event, context):
    dynamo = boto3.client("dynamodb")
    try:
        dynamo.delete_table(
            TableName=os.environ["TABLE_NAME"]
        )
        return ResponseUtils.success(200, "Tabla eliminada con éxito")
    except botocore.exceptions.ClientError as e:
        print(e.response["Error"]["Code"])
        return ResponseUtils.error(500, "La tabla no existe")
