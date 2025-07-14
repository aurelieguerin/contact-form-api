import json
import boto3
import os
from datetime import datetime
from uuid import uuid4

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get("TABLE_NAME")  # Will be injected from SAM template
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        name = body.get("name")
        email = body.get("email")
        message = body.get("message")

        if not (name and email and message):
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing name, email, or message"})
            }

        # Create a new item with UUID
        item = {
            "id": str(uuid4()),
            "name": name,
            "email": email,
            "message": message,
            "timestamp": datetime.utcnow().isoformat()
        }

        # Store the item in DynamoDB
        table.put_item(Item=item)

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Message received successfully!"})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }