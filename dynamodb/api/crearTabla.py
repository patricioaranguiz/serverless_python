import boto3
import botocore
import os
from utils.responseUtils import ResponseUtils


def handler(event, context):
    dynamodb = boto3.client("dynamodb")
    try:
        table = dynamodb.create_table(
            TableName=os.environ['TABLE_NAME'],
            KeySchema=[
                {
                    'AttributeName': 'ID',
                    'KeyType': 'HASH'  # Partition key
                },
                # Si es necesario crear la tabla con un orden, se debe descomentar las lineas siguientes
                # {
                #     'AttributeName': 'Nombre',
                #     'KeyType': 'RANGE'  # Sort key
                # }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'ID',
                    'AttributeType': 'S'
                },
                # Si es necesario crear la tabla con un orden, se debe descomentar las lineas siguientes
                # {
                #     'AttributeName': 'Nombre',
                #     'AttributeType': 'S'
                # },

            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            },
            Tags=[
                {
                    'Key': 'Proyecto',
                    'Value': 'Aprendizaje'
                },
            ]
        )
        print(table)
        return ResponseUtils.success(200, "Tabla creada con exito")

    except botocore.exceptions.ClientError as e:
        print(e.response["Error"]["Code"])
        if e.response["Error"]["Code"] == "ResourceInUseException":
            return ResponseUtils.error(500, "La tabla ya existe")
