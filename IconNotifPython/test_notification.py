# coding=utf-8

import notification_data
import utilities

DEVICE_IP = '192.168.43.67'

DISPLAY_URL = 'http://' + DEVICE_IP + ':8080/displays/10/'


def display_all_notifications(all_notifications):
    count = 0
    while count < len(all_notifications):
        notification_data = all_notifications[count].copy()
        utilities.send_request(DISPLAY_URL, notification_data['text'])
        utilities.sleep_seconds(4)
        utilities.send_request(DISPLAY_URL, notification_data['image'])
        utilities.sleep_seconds(4)

        count += 1
    utilities.send_request(DISPLAY_URL, {"subheading": ""})


display_all_notifications(notification_data.get_all_testing_notifications())
