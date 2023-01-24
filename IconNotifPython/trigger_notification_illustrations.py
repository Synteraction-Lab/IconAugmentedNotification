# coding=utf-8

import notification_data
import participant_config
import device_config

import sys
import threading
import time
import traceback
import utilities
from random import randint

START_NOTIFICATION_GAP_SECONDS = 8

MINIMUM_NOTIFICATION_GAP_SECONDS = 17
MAXIMUM_NOTIFICATION_GAP_SECONDS = 26
NOTIFICATION_DISPLAY_SECONDS = 10

TRAINING_GAP_SHIFT_SECONDS = -5  # should be less than MINIMUM_NOTIFICATION_GAP_SECONDS


DEVICE_IP = device_config.get_device_ip()


NOTIFICATION_URL = 'http://' + DEVICE_IP + ':8080/notifiers/12/'
DISPLAY_URL = 'http://' + DEVICE_IP + ':8080/displays/10/'

NOTIFICATION_TYPE_NONE = 'none'

NOTIFICATIONS_PER_TRAINING_SESSION = 3
NOTIFICATIONS_PER_TESTING_SESSION = 6

MAX_RETRY_ATTEMPT = 3

NOTIFICATION_KEY_ID = "id"
NOTIFICATION_KEY_SEND_START_TIME = "send_start_time"
NOTIFICATION_KEY_SEND_COMPLETE_TIME = "send_complete_time"
NOTIFICATION_KEY_SEND_SUCCESS = "send_success"
NOTIFICATION_KEY_DATA = "data"

TIMING_KEY_TRIAL = "trial"
TIMING_KEY_GLOBAL_TIME = "global_time"
TIMING_KEY_TASK_TIME = "task_time"


def send_notification_data(notification):
    attempt = 0
    success = False
    while not success and attempt < MAX_RETRY_ATTEMPT:
        success = utilities.send_request(DISPLAY_URL, notification)
        attempt += 1

        if not success and attempt < MAX_RETRY_ATTEMPT:
            utilities.sleep_seconds(0.8)

    return success


def clear_notification_data():
    send_notification_data({"subheading": ""})


scheduled_send_time = 0


#
# global_clock: use `getTime()` method to log time
def trigger_notification_randomly(participant, session, global_clock):
    global scheduled_send_time
    global flag_is_running

    notification_data.shuffle_data()

    notification_type = participant_config.get_config(participant, session)
    print(
        f'participant: {participant}, session: {session}, start_time: {global_clock.getTime()}, type:{notification_type}')

    # skip no-notification condition
    if notification_data.is_no_notification(notification_type):
        print('Skipping no-notification condition')
        return

    # sessions: training -> [0, -1, -2],  testing -> [1,2]
    notification_limit = NOTIFICATIONS_PER_TESTING_SESSION
    training = False
    if int(session) < 0:
        notification_limit = NOTIFICATIONS_PER_TRAINING_SESSION
        training = True

    notification_count = 0

    current_time = time.time()
    sent_time = 0
    scheduled_send_time = current_time + START_NOTIFICATION_GAP_SECONDS + randint(
        MINIMUM_NOTIFICATION_GAP_SECONDS,
        MAXIMUM_NOTIFICATION_GAP_SECONDS)

    print('Starting sending notifications: ', notification_limit)
    should_clear = False
    while (notification_count < notification_limit or should_clear) and flag_is_running:

        current_time = time.time()

        if current_time > scheduled_send_time:

            notification_count += 1
            scheduled_send_time = current_time + NOTIFICATION_DISPLAY_SECONDS + randint(
                MINIMUM_NOTIFICATION_GAP_SECONDS, MAXIMUM_NOTIFICATION_GAP_SECONDS)
            # add the shift for training
            if training:
                scheduled_send_time += TRAINING_GAP_SHIFT_SECONDS

            log_info(
                f'Notification: {notification_count}, current: {current_time}, schedule: {scheduled_send_time}')

            # get notification
            if training:
                notification = notification_data.get_next_notification_training_data(
                    notification_type)
            else:
                notification = notification_data.get_next_notification_testing_data(
                    notification_type)

            # update notification image, if it has an image
            icon_image = notification.get("image")
            if icon_image is not None:
                icon_info = icon_image.split()  # <color> <icon_name>
                updated_icon_info = f'{icon_info[0]} {icon_info[1]}{participant_config.get_icon_suffix(participant, icon_info[1])}'
                notification["image"] = updated_icon_info

            # send notification
            notification[NOTIFICATION_KEY_SEND_START_TIME] = global_clock.getTime()
            success = send_notification_data(notification)
            should_clear = True

            # log event time
            current_time = time.time()
            sent_time = current_time

            notification[NOTIFICATION_KEY_SEND_COMPLETE_TIME] = global_clock.getTime()
            notification[NOTIFICATION_KEY_SEND_SUCCESS] = success
            log_notification(participant, session, notification)
            # log_info(notification)

        if current_time > sent_time + NOTIFICATION_DISPLAY_SECONDS:
            # clear the notification
            clear_notification_data()
            should_clear = False
            sent_time = scheduled_send_time
            log_info(f'clear: {current_time}')

        # sleep
        utilities.sleep_seconds(0.01)

    print(f'Stopping sending notifications:: participant: {participant}, session: {session}, type:{notification_type}')

    if not flag_is_running:
        clear_notification_data()
    flag_is_running = False


def log_info(message):
    # pass
    print(message)


def log_notification(participant, session, notification):
    file_name = f'data/{participant}/{participant}_{session}_notifications.csv'

    if not utilities.is_file_exists(file_name):
        utilities.append_data(file_name,
                              f'{NOTIFICATION_KEY_ID},{NOTIFICATION_KEY_SEND_START_TIME}'
                              f',{NOTIFICATION_KEY_SEND_COMPLETE_TIME}'
                              f',{NOTIFICATION_KEY_SEND_SUCCESS}'
                              f',{NOTIFICATION_KEY_DATA}\n')
    notification_info = '"' + f'{notification}'.replace('"', '""') + '"'
    # print(notification_info)
    utilities.append_data(file_name,
                          f'{notification[NOTIFICATION_KEY_ID]}'
                          f',{notification[NOTIFICATION_KEY_SEND_START_TIME]}'
                          f',{notification[NOTIFICATION_KEY_SEND_COMPLETE_TIME]}'
                          f',{notification[NOTIFICATION_KEY_SEND_SUCCESS]}'
                          f',{notification_info}\n')


def log_timing(participant, session, trial, global_time, task_time):
    file_name = f'data/{participant}/{participant}_{session}_timing.csv'

    if not utilities.is_file_exists(file_name):
        utilities.append_data(file_name,
                              f'{TIMING_KEY_TRIAL},{TIMING_KEY_GLOBAL_TIME},{TIMING_KEY_TASK_TIME}\n')

    utilities.append_data(file_name, f'{trial},{global_time},{task_time}\n')


def log_all_timing(participant, session, data):
    file_name = f'data/{participant}/{participant}_{session}_timing.csv'

    if not utilities.is_file_exists(file_name):
        utilities.append_data(file_name,
                              f'{TIMING_KEY_TRIAL},{TIMING_KEY_GLOBAL_TIME},{TIMING_KEY_TASK_TIME}\n')

    utilities.append_data(file_name, data)


def log_timing_threaded(participant, session, trial, global_time, task_time):
    threading.Thread(target=log_timing,
                     args=(participant, str(int(session)), trial, global_time, task_time)).start()


def trigger_notification_randomly_with_exception(participant, session, global_clock):
    try:
        trigger_notification_randomly(participant, session, global_clock)
    except Exception:
        print("Unhandled exception")
        traceback.print_exc(file=sys.stdout)


flag_is_running = False


def trigger_notification_randomly_threaded(participant, session, global_clock):
    global flag_is_running

    if not flag_is_running:
        flag_is_running = True
        threading.Thread(target=trigger_notification_randomly_with_exception,
                         args=(participant, str(int(session)), global_clock)).start()
        print("Starting triggering!")
    else:
        print("Triggering is running!")


def cancel_notification_trigger():
    global flag_is_running

    flag_is_running = False

# ## testing
# trigger_notification_randomly_threaded('p1', '1', 0.0)
