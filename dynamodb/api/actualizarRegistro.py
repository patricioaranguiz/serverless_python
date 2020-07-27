import boto3
import botocore
import os
from utils.responseUtils import ResponseUtils


def handler(event, context):
    dynamo = boto3.client("dynamodb")
    try:
        response = dynamo.update_item(
            ExpressionAttributeNames={
                '#Nom': 'Nombre',
                '#Anno': 'Anno',
            },
            ExpressionAttributeValues={
                ':n': {
                    'S': 'Louder Than Ever',
                },
                ':a': {
                    'N': '2015',
                },
            },
            Key={
                'ID': {
                    'S': '',  # ID de registro en la tabla
                },
            },
            ReturnValues='ALL_NEW',
            TableName=os.environ["TABLE_NAME"],
            UpdateExpression='SET #Anno = :a, #Nom = :n',
        )

        print(response)
        return ResponseUtils.success(200, "Registro actualizado con exito")
    except botocore.exceptions.ClientError as e:
        print(e.response["Error"]["Code"])
        return ResponseUtils.error(500, str(e.response["Error"]["Message"]))

