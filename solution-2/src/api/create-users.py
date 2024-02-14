import json

def handler (event, context):
    print(f'Objects are {event}, {context}')
    return {
       "statusCode": 200,
       "body": json.dumps({
            "message": "maze hi maze"
       })
    }