def handler(event, context):
    print(event)
    return {"code": 200, "body": "Hello World!"}