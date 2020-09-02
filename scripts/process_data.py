import json
from datetime import datetime
import logging


def convert_timestamp(timestamp):
    return datetime.fromtimestamp(int(timestamp))


if __name__ == '__main__':

    alarms_dict = {}

    with open('../resources/alarms.json') as input_file:
        alarms = json.load(input_file)

    for alarm in alarms:
        date_time = convert_timestamp(alarm['alarm_time'])
        alarm['alarm_date'] = str(date_time.date())
        alarm['alarm_time'] = str(date_time.time())

        # converts the list into dict
        alarms_dict.setdefault(alarm['alarm_date'], []).append(alarm)

    with open('../resources/alarms_processed.json', 'w') as output_file:
        json.dump(alarms_dict, output_file)



