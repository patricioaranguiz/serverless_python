import boto3
import botocore
import os
from utils.responseUtils import ResponseUtils
import uuid


def handler(event, context):
    dynamo = boto3.client("dynamodb")
    try:
        response = dynamo.put_item(
            Item={
                'ID': {
                    'S': str(uuid.uuid1()),
                },
                'Nombre': {
                    'S': 'Jobs',
                },
                'Anno': {
                    'S': '1995',
                },
            },
            ReturnConsumedCapacity='TOTAL',
            TableName=os.environ["TABLE_NAME"],
        )
        print(response)
        return ResponseUtils.success(200, "Registro insertado con exito")
    except botocore.exceptions.ClientError as e:
        print(e.response["Error"]["Code"])
        ResponseUtils.error(500, e.response["Error"]["Message"])
