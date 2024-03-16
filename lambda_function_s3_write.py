import json
import boto3


def lambda_handler(event, context):
    event_data = json.dumps(event)

    # Define the S3 bucket and key where you want to store the data
    # bucket_name = 'your-bucket-name'
    # key = 'event_data.json'  # Example key name
    print(event_data)
    # Create an S3 client
    s3_client = boto3.client('s3')

    # Write the event data to the S3 bucket
    try:
        response = s3_client.put_object(
            Body=event_data,
            Bucket='hk-airbnb-booking-records',
            Key='hk-airbnb-booking-records.csv'
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
