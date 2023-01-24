# coding=utf-8

import notification_data
import device_config
import utilities

DEVICE_IP = device_config.get_device_ip()

DISPLAY_URL = 'http://' + DEVICE_IP + ':8080/displays/10/'


def display_all_notifications(all_notifications):
    count = 0
    while count < len(all_notifications):
        notification_data = all_notifications[count].copy()
        if notification_data.get('text_long') is not None:
            utilities.send_request(DISPLAY_URL, notification_data.get('text_long'))
            utilities.sleep_seconds(4)
        if notification_data.get('image_long') is not None:
            utilities.send_request(DISPLAY_URL, notification_data.get('image_long'))
            utilities.sleep_seconds(4)
        if notification_data.get('text_short') is not None:
            utilities.send_request(DISPLAY_URL, notification_data.get('text_short'))
            utilities.sleep_seconds(4)
        if notification_data.get('image_short') is not None:
            utilities.send_request(DISPLAY_URL, notification_data.get('image_short'))
            utilities.sleep_seconds(4)

        count += 1
    utilities.send_request(DISPLAY_URL, {"subheading": ""})


display_all_notifications(notification_data.get_all_testing_notifications())
