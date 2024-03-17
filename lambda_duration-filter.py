import json
from datetime import datetime


def calculate_duration(start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    duration = (end_date - start_date).days
    return duration


def lambda_handler(event, context):
    sqs_records = event
    enriched_events = []

    for record in sqs_records:
        # Perform enrichment (e.g., add a timestamp field)
        enriched_data = json.loads(record['body'])

        if calculate_duration(enriched_data["startDate"], enriched_data["endDate"]) > 1:
            enriched_events.append({
                'version': '0',
                'id': record['messageId'],
                'detail-type': 'EnrichedEvent',
                'source': 'Custom.Enrichment',
                'account': record['eventSourceARN'].split(':')[4],
                'time': record['attributes']['SentTimestamp'],
                'region': record['awsRegion'],
                'resources': [],
                'detail': enriched_data
            })
    print("events processing after applying duration filter", str(enriched_events))
    return enriched_events
