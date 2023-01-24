# coding=utf-8

# command format: python3 txt_to_csv_illustrations.py -p <PARTICIPANT_ID> -s <SESSION_ID>

import numpy as np
import optparse
import pandas as pd
import stimuli_generation
import utilities

TESTING_SESSION_IDS = [1, 2, 3, 4]

NOTIFICATION_DURATION_MS = 10 * 1000
STIMULI_DURATION_MS = 625
HIT_TOLERANCE_DURATION_MS = 2000

HIT_TOLERANCE_INDICES = HIT_TOLERANCE_DURATION_MS // STIMULI_DURATION_MS  # i.e.  3 * 625 ms ~ 1900 ms, 625 ms is the stimuli duration
NOTIFICATION_DURATION_INDICES = NOTIFICATION_DURATION_MS // STIMULI_DURATION_MS  # i.e. 17 * 625 ~ 10 s

CLICK_EXPECTED_IMAGE_IDS = stimuli_generation.get_stimuli_image_ids()
NOISE_STIMULI_TYPES = stimuli_generation.get_noise_stimuli()
NOISE_STIMULI_DURATION_INDICES = stimuli_generation.get_noise_stimuli_size()

# input: data directory
DATA_DIRECTORY_FORMAT = 'data/{}'  # {participant}

# input: related to stimuli response
FILE_NAME_STIMULI_RESPONSE_FORMAT = '{}_{}_task_vigilance'

COLUMN_STIMULI_STIMULI_TIME = 'im.started'
COLUMN_STIMULI_CLICK_TIMES = 'mouse.time'
COLUMN_STIMULI_IMAGE_ID = 'image_id'
COLUMN_STIMULI_TYPE = 'stimuli_type'
COLUMN_STIMULI_TRIAL_ID = 'trials.thisRepN'
COLUMN_STIMULI_ID = 'stimuli_id'

# input: related to notification stimuli
FILE_NAME_NOTIFICATION_STIMULI_FORMAT = '{}_{}_notifications'

COLUMN_NOTIFICATION_ID = 'id'
COLUMN_NOTIFICATION_SEND_START_TIME = 'send_start_time'
COLUMN_NOTIFICATION_SEND_COMPLETE_TIME = 'send_complete_time'
COLUMN_NOTIFICATION_SEND_SUCCESS = 'send_success'

# input: related to timing info
FILE_NAME_TIMING_INFO_FORMAT = '{}_{}_timing'

COLUMN_TIMING_TRIAL = 'trial'
COLUMN_TIMING_GLOBAL_TIME = 'global_time'
COLUMN_TIMING_TASK_TIME = 'task_time'

# output: converted file
FILE_NAME_CONVERTED_DATA_FORMAT = 'data/{}/{}_{}_converted.csv'


def read_csv_file_with_header(csv_file):
    return pd.read_csv(csv_file, header=0)


def process_participant_session(participant, session):
    print(f'Participant: {participant}, session: {session}')
    data_directory = DATA_DIRECTORY_FORMAT.format(participant)
    # image stimuli and click data
    image_stimuli_response_files = utilities.read_file_names(data_directory, '.csv',
                                                             FILE_NAME_STIMULI_RESPONSE_FORMAT.format(
                                                                 participant, session))
    data_frame_image_stimuli_response = read_csv_file_with_header(image_stimuli_response_files[0])
    # print(data_frame_image_stimuli_response.shape)
    image_repeat_count = data_frame_image_stimuli_response.shape[
                             0] - 1  # = number of rows after removing last entry for 'stop' text

    ori_round = data_frame_image_stimuli_response[COLUMN_STIMULI_TRIAL_ID]
    ori_image_stimuli = data_frame_image_stimuli_response[COLUMN_STIMULI_IMAGE_ID]
    ori_stimuli_type = data_frame_image_stimuli_response[COLUMN_STIMULI_TYPE]
    # ori_click_times are w.r.t task
    ori_image_stimuli_time = np.array(
        data_frame_image_stimuli_response[COLUMN_STIMULI_STIMULI_TIME])
    # click_times are w.r.t global clock
    ori_click_times = data_frame_image_stimuli_response[COLUMN_STIMULI_CLICK_TIMES]
    # print(ori_click_times)

    click_times = [float(str_time.replace('[', '').replace(']', '')) for str_time in ori_click_times
                   if str_time != '[]' and pd.notna(str_time)]
    # print(click_times)

    # timing data for synchronization
    timing_info_files = utilities.read_file_names(data_directory, '.csv',
                                                  FILE_NAME_TIMING_INFO_FORMAT.format(participant,
                                                                                      session))
    data_frame_timing_info = read_csv_file_with_header(timing_info_files[0])
    experiment_time_shift = np.array(data_frame_timing_info[COLUMN_TIMING_TASK_TIME]) - np.array(
        data_frame_timing_info[COLUMN_TIMING_GLOBAL_TIME])  # 1D array for each trial
    # print(data_frame_timing_info, experiment_time_shift)

    # time shift for synchronization
    image_stimuli_time = ori_image_stimuli_time.copy()[0:-1]  # remove the last entry with 'nan'
    if len(experiment_time_shift) > 1:
        image_stimuli_time -= experiment_time_shift[1:]
    else:
        image_stimuli_time -= experiment_time_shift[0]
        print(' ** Only 1 values found for time syncing')
    # print(image_stimuli_time)

    # notification stimuli data
    notification_stimuli_files = utilities.read_file_names(data_directory, '.csv',
                                                           FILE_NAME_NOTIFICATION_STIMULI_FORMAT.format(
                                                               participant, session))
    notification_count = 0
    notification_stimuli_time = []
    if len(notification_stimuli_files) > 0:  # if there is any data file
        data_frame_notifications = read_csv_file_with_header(notification_stimuli_files[0])
        notification_count = data_frame_notifications.shape[0]
        notification_stimuli_time = np.array(
            data_frame_notifications[COLUMN_NOTIFICATION_SEND_START_TIME])

    # print(f'click_times:{click_times}, image_stimuli_time: {image_stimuli_time}, notification_count: {notification_count}, notification_stimuli_time: {notification_stimuli_time}')

    mapped_click_time = []
    click_time_count = len(click_times)
    index_click_time = 0

    mapped_notification_time = []
    index_notification_time = 0

    # align stimuli, click and notification time
    for image_time in image_stimuli_time:
        if index_click_time < click_time_count and click_times[index_click_time] < image_time:
            mapped_click_time.append(click_times[index_click_time])
            index_click_time += 1
        else:
            mapped_click_time.append(None)

        if index_notification_time < notification_count and notification_stimuli_time[
            index_notification_time] < image_time:
            mapped_notification_time.append(notification_stimuli_time[index_notification_time])
            index_notification_time += 1
        else:
            mapped_notification_time.append(None)

        # if index_click_time >= click_time_count and index_notification_time >= notification_count:
        #     break

    # print(mapped_click_time, mapped_notification_time)

    # calculate hit, miss, false alarm, reaction time
    hit = []
    miss = []
    false_alarm = []
    correct_rejection = []
    reaction_time = []

    prev_stimuli_type = None

    total_stimuli_count = len(image_stimuli_time)
    for index in range(total_stimuli_count):
        # hit or miss
        if ori_image_stimuli[index] in CLICK_EXPECTED_IMAGE_IDS:
            hit_click_indices = [click_index for click_index in
                                 range(index,
                                       min(index + HIT_TOLERANCE_INDICES, total_stimuli_count))
                                 if mapped_click_time[click_index] is not None]
            if len(hit_click_indices) > 0:
                hit.append(1)
                miss.append(None)
                rt_instance = mapped_click_time[hit_click_indices[0]] - image_stimuli_time[index]
                if rt_instance < 0:
                    print(f' *** Negative reaction time: {rt_instance}, index: {index}')
                reaction_time.append(abs(rt_instance))
            else:
                hit.append(None)
                miss.append(1)
                reaction_time.append(None)
        else:
            hit.append(None)
            miss.append(None)
            reaction_time.append(None)

        # false alarm
        if mapped_click_time[index] is not None:
            hit_stimuli_indices = [stimuli_index for stimuli_index in
                                   range(index, max(0, index - HIT_TOLERANCE_INDICES), -1) if
                                   ori_image_stimuli[stimuli_index] in CLICK_EXPECTED_IMAGE_IDS]
            if len(hit_stimuli_indices) > 0:
                false_alarm.append(None)
            else:
                false_alarm.append(1)
        else:
            false_alarm.append(None)

        # correct rejection
        current_stimuli_type = ori_stimuli_type[index]
        if current_stimuli_type != prev_stimuli_type and current_stimuli_type in NOISE_STIMULI_TYPES:
            clicks_during_noise = [click_index for click_index in range(index, min(
                index + NOISE_STIMULI_DURATION_INDICES, total_stimuli_count)) if
                                   mapped_click_time[click_index] is not None]
            if len(clicks_during_noise) == 0:
                correct_rejection.append(1)
            else:
                correct_rejection.append(0)
        else:
            correct_rejection.append(None)

        prev_stimuli_type = current_stimuli_type

    # calculate total hit, miss, false alarm, (average) reaction time during notification
    hit_sum_notification = [None] * total_stimuli_count
    miss_sum_notification = [None] * total_stimuli_count
    false_alarm_sum_notification = [None] * total_stimuli_count
    correct_rejection_sum_notification = [None] * total_stimuli_count
    reaction_time_avg_notification = [None] * total_stimuli_count

    notification_indices = [index for index in range(total_stimuli_count) if
                            mapped_notification_time[index] is not None]
    for notification_start_index in notification_indices:
        notification_end_index = min(notification_start_index + NOTIFICATION_DURATION_INDICES,
                                     total_stimuli_count)
        hit_sum_notification[notification_start_index] = np.sum(get_array_without_none(
            hit[notification_start_index: notification_end_index]))
        miss_sum_notification[notification_start_index] = np.sum(get_array_without_none(
            miss[notification_start_index: notification_end_index]))
        false_alarm_sum_notification[notification_start_index] = np.sum(get_array_without_none(
            false_alarm[notification_start_index: notification_end_index]))
        reaction_time_avg_notification[notification_start_index] = np.sum(get_array_without_none(
            correct_rejection[notification_start_index: notification_end_index]))
        reaction_time_avg_notification[notification_start_index] = np.mean(get_array_without_none(
            reaction_time[notification_start_index: notification_end_index]))

        # print(hit_sum_notification[notification_start_index],
        #       miss_sum_notification[notification_start_index],
        #       false_alarm_sum_notification[notification_start_index],
        #       reaction_time_avg_notification[notification_start_index],
        #       reaction_time_avg_notification[notification_start_index: notification_end_index])

    csv_data = {'round': ori_round[0:-1],
                'type': ori_stimuli_type[0:-1],
                'image': ori_image_stimuli[0:-1],
                'start_time': image_stimuli_time,
                'click_time': mapped_click_time,
                'notification_time': mapped_notification_time,
                'hit': hit,
                'miss': miss,
                'false_alarm': false_alarm,
                'correct_rejection': correct_rejection,
                'reaction_time': reaction_time,
                'hit-sum-notification': hit_sum_notification,
                'miss-sum-notification': miss_sum_notification,
                'false_alarm-sum-notification': false_alarm_sum_notification,
                'correct_rejection-sum-notification': correct_rejection_sum_notification,
                'reaction_time-avg-notification': reaction_time_avg_notification,
                'ori.stimuli_time': ori_image_stimuli_time[0:-1],
                'ori.click_time': ori_click_times[0:-1]}
    # print(csv_data)
    converted_file_name = FILE_NAME_CONVERTED_DATA_FORMAT.format(participant, participant, session)
    pd.DataFrame(data=csv_data).to_csv(converted_file_name)
    print(f'\nData is written to [{converted_file_name}]')

    print_stats(click_time_count, csv_data)


def print_stats(click_count, csv_data):
    print(f'\t[Clicks: {click_count}] '
          f'Hit: {np.sum(get_array_without_none(csv_data["hit"]))}, '
          f'Miss: {np.sum(get_array_without_none(csv_data["miss"]))}, '
          f'False Alarm: {np.sum(get_array_without_none(csv_data["false_alarm"]))}, '
          f'Correct Rejection: {np.sum(get_array_without_none(csv_data["correct_rejection"]))}'
          f'\n')
    pass


def get_array_without_none(array):
    return [item for item in array if item is not None]


def process_participant(participant):
    for session in TESTING_SESSION_IDS:
        process_participant_session(participant, session)


parser = optparse.OptionParser()
parser.add_option("-p", "--participant", dest="participant")
parser.add_option("-s", "--session", dest="session")

options, args = parser.parse_args()

# print options
# print args
_participant = options.participant
_session = options.session

if _session is None:
    process_participant(_participant)
else:
    process_participant_session(_participant, _session)
