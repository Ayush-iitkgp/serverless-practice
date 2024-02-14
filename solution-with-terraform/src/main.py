import json
from camel_converter import to_snake


def lambda_handler(event, context):
    print(f"Event is {event}")
    print(f"Context is {context}")
    body = event.get('body', None)

    if body:
        return {
            'statusCode': 200,
            'body': json.dumps({
                "items": to_snake("Hello World")
            })
        }

