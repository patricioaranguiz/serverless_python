import json


class ResponseUtils:

    def success(code, texto):
        return {"statusCode": code, "body": json.dumps(texto)}

    def error(code, texto):
        return {"statusCode": code, "body": json.dumps(texto)}
