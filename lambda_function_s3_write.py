import json
import boto3
from datetime import datetime


def lambda_handler(event, context):
    event_data = json.loads(event[0]["body"])
    print(event_data)
    # Create an S3 client
    s3_client = boto3.client('s3')
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    s3_key = f"hk-airbnb-booking-records-{timestamp}.json"
    event_body = json.dumps(event_data)
    try:
        response = s3_client.put_object(
            Body=event_body,
            Bucket='hk-airbnb-booking-records',
            Key=s3_key
        )
        print("Event data has been written to S3 successfully.")
        return {
            'statusCode': 200,
            'body': json.dumps('Event data has been written to S3 successfully.')
        }
    except Exception as e:
        print(f"Error writing data to S3: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error writing data to S3: {str(e)}')
        }
