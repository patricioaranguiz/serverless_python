"""
En este servicio se ve la ejecución de obtener los objetos de un bucket
"""
import json
import boto3
import os
import botocore


def handler(event, context):
    # Nombre del Bucket
    bucketName = os.environ['BUCKET_NAME']
    response = {}

    # Se declara una lista vacía
    listadoArchivos = []

    # Referenciamos el recurso a utilizar de la librería boto3
    s3 = boto3.client("s3")

    try:
        # Buscamos todos los archivos dentro del Bucket
        archivos = s3.list_objects(Bucket=bucketName)
        try:
            contents = archivos["Contents"]
            for obj in contents:
                listadoArchivos.append({'nombreArchivo': obj["Key"], 'size': obj["Size"]})
        except KeyError:
            print("No existen contenidos en el bucket")

        response = {
            "statusCode": 200,
            "body": json.dumps(listadoArchivos)
        }

    except botocore.exceptions.ClientError as e:
        print (e)
        if e.response["Error"]["Code"] == "NoSuchBucket":
            response = {
                "statusCode": 500,
                "body": "Bucket no encontrado"
            }

    # Retornamos la lista de archivos
    return response
