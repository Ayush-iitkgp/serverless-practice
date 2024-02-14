import json
from caseconverter import camelcase


def handler (event, context):
    query_params = event.get('queryParameters', '')
    print(f'Objects are {query_params}')
    return {
       "statusCode": 200,
       "body": json.dumps({
            "message": camelcase("Hello, world!")
       })
    }

# if __name__ == '__main__':
#    handler({}, {})