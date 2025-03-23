# function to send CSV data to Azure Event Hub
from azure.eventhub import EventHubProducerClient, EventData
import csv
import json

from utilities import EVENT_HUB_CONNECTION_STR, EVENT_HUB_NAME

def main():
    # create the producer client
    producer_client = EventHubProducerClient.from_connection_string(
        conn_str=EVENT_HUB_CONNECTION_STR,
        eventhub_name=EVENT_HUB_NAME
    )

    with open('data/weather_data_batch1.csv', 'r') as f:
        csv_reader = csv.reader(f)

        for i, row in enumerate(csv_reader):
            # skip the header
            if i == 0:
                continue

            # print(row)
            event_data = json.dumps(row)

            # send to Azure Event Hub
            print(f'Sending Row {i+1} to Azure Event Hub named {EVENT_HUB_NAME}...')
            producer_client.send_event(EventData(event_data))

    producer_client.close()


if __name__ == '__main__':
    main()