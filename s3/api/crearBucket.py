import boto3
import os
import botocore

s3 = boto3.client("s3")


def handler(event, context):
    # Se obtiene el nombre del bucket desde el archivo enviroment.
    bucketName = os.environ['BUCKET_NAME']

    try:
        response = s3.create_bucket(
            ACL='private',  # 'private'|'public-read'|'public-read-write'|'authenticated-read'
            Bucket=str(bucketName),
            CreateBucketConfiguration={
                'LocationConstraint': 'us-west-1'
                # 'EU'|'eu-west-1'|'us-west-1'|'us-west-2'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1'|'cn-north-1'|'eu-central-1'
            }
        )
        print(response)
        respuesta = {
            "statusCode": 200,
            "body": "Bucket creado correctamente"
        }
    except botocore.exceptions.ClientError as e:
        if (e.response["Error"]["Code"] == "BucketAlreadyOwnedByYou"
                or e.response["Error"]["Code"] == "BucketAlreadyExists"):
            respuesta = {
                "statusCode": 500,
                "body": "El Bucket ya existe"
            }

    return respuesta
