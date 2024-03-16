import json
import boto3
import random
import uuid
from datetime import datetime, timedelta

sqs_client = boto3.client('sqs')
QUEUE_URL = 'arn:aws:sqs:us-east-2:992382818239:AirbnbBookingQueue'

cities = ["New York", "Los Angeles", "London", "Paris", "Tokyo", "Sydney"]
countries = ["USA", "UK", "France", "Japan", "Australia", "Canada"]


# Function to generate a random UUID
def generate_uuid():
    return str(uuid.uuid4())


# Function to generate a random UserID
def generate_user_id():
    return f"User{random.randint(1000, 9999)}"


# Function to generate a random PropertyID
def generate_property_id():
    return f"Property{random.randint(10000, 99999)}"


# Function to generate a random location
def generate_location():
    city = random.choice(cities)
    country = random.choice(countries)
    return f"{city}, {country}"


# Function to generate a random date in YYYY-MM-DD format
def generate_date():
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2023, 12, 31)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime('%Y-%m-%d')


# Function to generate a random price
def generate_price():
    return round(random.uniform(50, 500), 2)


def lambda_handler(event, context):
    i = 0
    while i < 200:
        booking_data = {
            "bookingId": generate_uuid(),
            "userId": generate_user_id(),
            "propertyId": generate_property_id(),
            "location": generate_location(),
            "startDate": generate_date(),
            "endDate": generate_date(),
            "price": generate_price()
        }
        print(booking_data)
        sqs_client.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps(booking_data)
        )
        i += 1

    return {
        'statusCode': 200,
        'body': json.dumps('Sales order data published to SQS!')
    }
