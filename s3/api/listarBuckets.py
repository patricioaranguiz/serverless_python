import boto3
import json

"""
Función que obtiene el listado de los buckets creados
"""


def handler(event, context):
    s3 = boto3.client("s3")

    # Se declara el el listado vacío.
    listado = []

    try:
        # Se hace la llamada
        response = s3.list_buckets()

        # Se realiza un bucle para agregar los bucket encontrados a la lista antes declarada
        for bucket in response["Buckets"]:
            listado.append(bucket["Name"])

        response = {
            "statusCode": 200,
            "body": json.dumps(listado)
        }

    except KeyError as e:
        print(e)
        response = {
            "statusCode": 500,
            "body": "Ocurrio un error al intentar obtener el listado de buckets"
        }

    return response
