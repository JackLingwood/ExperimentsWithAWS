# lambda_function.py
def lambda_handler(event, context):
    print("Received event: " + str(event))
    return {
        "statusCode": 200,
        "body": "Hello from CLI Lambda!"
    }