# coding=utf-8

import device_config
import utilities

DEVICE_IP = device_config.get_device_ip()


DISPLAY_URL = 'http://' + DEVICE_IP + ':8080/displays/10/'
NOTIFICATION_URL = 'http://' + DEVICE_IP + ':8080/notifiers/12/'

NOTIFICATION_DISPLAY_SECONDS = 4

MAX_RETRY_ATTEMPT = 4


def send_display_data(display_data):
    attempt = 0
    success = False
    while not success and attempt < MAX_RETRY_ATTEMPT:
        success = utilities.send_request(DISPLAY_URL, display_data)
        attempt += 1

        if not success and attempt < MAX_RETRY_ATTEMPT:
            utilities.sleep_seconds(0.8)

    return success


def send_sample_text_display_data():
    send_display_data({"subheading": "This is a dummy notification"})


def send_sample_image_display_data():
    send_display_data({"subheading": "  5 min", "image": "#FF00FF7D call"})


counter = -1

def send_factor_data(factor):
    global counter

    data = []

    if factor == 'f': # familiarity
        data = [
            {"subheading": "  8 am", "image": "#FF00FF7D img_alarm6"},
            {"subheading": "  8 am", "image": "#FF00FF7D img_alarm1"},
            # {"subheading": "Alarm   8 am"},
        ]
    elif factor == 'd': # density
        data = [
            {"subheading": "Birthday   John"},
            {"subheading": "  John", "image": "#FF00FF7D img_birthday4"},
            {"subheading": "No left turn   7-9 am"},
            {"subheading": "  7-9 am", "image": "#FF00FF7D img_no_left_turn1"},
        ]
    elif factor == 'b': # brightness
        data = [
            {"subheading": "Doctor's appointment in 2 hours"},
            {"subheading": "  2 hrs", "image": "#FF00FF7D img_doctor4"},
        ]
    elif factor == 'w': # walking
        data = [
            # {"subheading": "Presentation   12 pm"},
            # {"subheading": "  12 pm", "image": "#FF00FF7D img_presentation2"},
            {"subheading": "Car   5 min"},
            {"subheading": "  5 min", "image": "#FF00FF7D img_car4"},
            # {"subheading": "Movie   Sunday"},
            # {"subheading": "  Sunday", "image": "#FF00FF7D img_movie4"},
            {"subheading": "Delivery   3 d"},
            {"subheading": "  3 d", "image": "#FF00FF7D img_delivery4"},
            # {"subheading": "Birthday   John"},
            # {"subheading": "  John", "image": "#FF00FF7D img_birthday4"},
            {"subheading": "Weight lifting   40 min"},
            {"subheading": "  40 min", "image": "#FF00FF7D img_exercise1"},
            {"subheading": "Valentine's day   2 d"},
            {"subheading": "  2 d", "image": "##FF00FF7D img_valentine_day4"},
            # {"subheading": "Backup computer   tonight"},
            # {"subheading": "  tonight", "image": "#FF00FF7D img_backup_computer4"},
            {"subheading": "Driving license   renew"},
            {"subheading": "  renew", "image": "#FF00FF7D img_licence1"},
            {"subheading": "Milk and eggs   Walmart"},
            {"subheading": "  Walmart", "image": "#FF00FF7D img_milk_eggs4"},
        ]

    counter += 1
    if counter >= len(data):
        counter = 0

    send_display_data(data[counter])




def clear_display_data():
    send_display_data({"subheading": ""})


_res = ''
while _res != 'n':
    _res = input("Continue? (n/t/i/c/f/d/b/w/r)")

    if _res == 't':
        send_sample_text_display_data()
        utilities.sleep_seconds(NOTIFICATION_DISPLAY_SECONDS)

    if _res == 'i':
        send_sample_image_display_data()
        utilities.sleep_seconds(NOTIFICATION_DISPLAY_SECONDS)


    if _res == 'f' or _res == 'd' or _res == 'b' or _res == 'w':
        send_factor_data(_res)
        utilities.sleep_seconds(NOTIFICATION_DISPLAY_SECONDS)

    if _res == 'r':
        counter = -1
        clear_display_data()

    # clear_display_data()
    if _res == 'c':
        clear_display_data()
