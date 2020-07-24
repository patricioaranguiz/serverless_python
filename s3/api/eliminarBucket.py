import os
import boto3
import botocore


def handler(event, context):
    s3 = boto3.client("s3")
    bucketName = os.environ['BUCKET_NAME']
    try:
        response = s3.delete_bucket(
            Bucket=bucketName
        )
        print(response)
        respuesta = {
            "statusCode": 200,
            "body": "Bucket eliminado correctamente"
        }
    except botocore.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "NoSuchBucket":
            respuesta = {
                "statusCode": 500,
                "body": "Bucket no encontrado"
            }

    return respuesta
