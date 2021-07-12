from .common.hello import world

def handler(event, context):
  return {
    "statusCode": 200,
    "body": world()
  }
