# coding=utf-8

import pandas as pd
from random import sample
from random import randint
from random import shuffle

TRIAL_DURATION_MS = 3.75 * 60 * 1000

IMAGE_DURATION_MS = 625

IMAGE_ID_1x1 = 1
IMAGE_ID_2x2 = 2
IMAGE_ID_1x2 = 3
IMAGE_ID_2x1 = 4

# STIMULI_TYPES = ["i1", "i2", "i3", "i4", "i5", "i6", "i7", "i8", "i9"]
STIMULI_TYPES = ["i1", "i2", "i3", "i4", "i5", "i6", "i9"]
NON_CONSECUTIVE_STIMULI = ['i9']

STIMULI_TYPES_COUNT = len(STIMULI_TYPES)
# STIMULI_IMAGE_ID_MAPPING = {
#     "i1": [IMAGE_ID_1x1, IMAGE_ID_2x1, IMAGE_ID_1x1, IMAGE_ID_2x2, IMAGE_ID_1x1, IMAGE_ID_2x2],
#     "i2": [IMAGE_ID_1x1, IMAGE_ID_1x2, IMAGE_ID_1x1, IMAGE_ID_2x2, IMAGE_ID_1x1, IMAGE_ID_2x2],
#     "i3": [IMAGE_ID_1x1, IMAGE_ID_2x2, IMAGE_ID_2x1, IMAGE_ID_2x2, IMAGE_ID_1x1, IMAGE_ID_2x2],
#     "i4": [IMAGE_ID_1x1, IMAGE_ID_2x2, IMAGE_ID_1x2, IMAGE_ID_2x2, IMAGE_ID_1x1, IMAGE_ID_2x2],
#     "i5": [IMAGE_ID_1x1, IMAGE_ID_2x2, IMAGE_ID_1x1, IMAGE_ID_2x1, IMAGE_ID_1x1, IMAGE_ID_2x2],
#     "i6": [IMAGE_ID_1x1, IMAGE_ID_2x2, IMAGE_ID_1x1, IMAGE_ID_1x2, IMAGE_ID_1x1, IMAGE_ID_2x2],
#     "i7": [IMAGE_ID_1x1, IMAGE_ID_2x2, IMAGE_ID_1x1, IMAGE_ID_2x2, IMAGE_ID_1x2, IMAGE_ID_2x2],
#     "i8": [IMAGE_ID_1x1, IMAGE_ID_2x2, IMAGE_ID_1x1, IMAGE_ID_2x2, IMAGE_ID_2x1, IMAGE_ID_2x2],
#     "i9": [IMAGE_ID_1x1, IMAGE_ID_2x2, IMAGE_ID_1x1, IMAGE_ID_2x2, IMAGE_ID_1x1, IMAGE_ID_2x2],
# }
STIMULI_IMAGE_ID_MAPPING = {
    "i1": [IMAGE_ID_1x1, IMAGE_ID_2x1, IMAGE_ID_2x2, IMAGE_ID_1x1, IMAGE_ID_2x2],
    "i2": [IMAGE_ID_1x1, IMAGE_ID_1x2, IMAGE_ID_2x2, IMAGE_ID_1x1, IMAGE_ID_2x2],
    "i3": [IMAGE_ID_1x1, IMAGE_ID_2x2, IMAGE_ID_2x1, IMAGE_ID_1x1, IMAGE_ID_2x2],
    "i4": [IMAGE_ID_1x1, IMAGE_ID_2x2, IMAGE_ID_1x2, IMAGE_ID_1x1, IMAGE_ID_2x2],
    "i5": [IMAGE_ID_1x1, IMAGE_ID_2x2, IMAGE_ID_1x1, IMAGE_ID_2x1, IMAGE_ID_1x1, IMAGE_ID_2x2],
    "i6": [IMAGE_ID_1x1, IMAGE_ID_2x2, IMAGE_ID_1x1, IMAGE_ID_1x2, IMAGE_ID_1x1, IMAGE_ID_2x2],
    "i9": [IMAGE_ID_1x1, IMAGE_ID_2x2, IMAGE_ID_1x1, IMAGE_ID_2x2],
}

IMAGES_PER_STIMULUS = len(STIMULI_IMAGE_ID_MAPPING["i1"])
STIMULI_DURATION_MS = IMAGES_PER_STIMULUS * IMAGE_DURATION_MS

TOTAL_STIMULI_COUNT = TRIAL_DURATION_MS // STIMULI_DURATION_MS

# assume each stimuli (i1 ... i6, ) has equal probability
# STIMULI_DISTRIBUTION = {
#     "i1": 1,
#     "i2": 1,
#     "i3": 1,
#     "i4": 1,
#     "i5": 1,
#     "i6": 1,
#     "i7": 1,
#     "i8": 1,
#     "i9": 1,
# }
STIMULI_DISTRIBUTION = {
    "i1": 1,
    "i2": 1,
    "i3": 2,
    "i4": 2,
    "i5": 1,
    "i6": 1,
    "i9": 1,
}

STIMULI_PER_ROUND = sum([STIMULI_DISTRIBUTION[stimulus_type] for stimulus_type in STIMULI_TYPES])


def get_stimuli_image_ids():
    return [IMAGE_ID_1x2, IMAGE_ID_2x1]


def get_noise_stimuli():
    return NON_CONSECUTIVE_STIMULI.copy()


def get_noise_stimuli_size():
    return len(STIMULI_IMAGE_ID_MAPPING[NON_CONSECUTIVE_STIMULI[0]])


def generate_new_stimuli_csv(csv_file_name):
    all_stimuli = []

    # select stimuli based on distribution
    stimuli_round = 0
    total_rounds = TOTAL_STIMULI_COUNT // STIMULI_PER_ROUND
    while stimuli_round < total_rounds:
        stimuli_round += 1
        temp_stimuli_per_round = []
        for stimulus in STIMULI_TYPES:
            temp_stimuli_per_round += STIMULI_DISTRIBUTION[stimulus] * [stimulus]

        shuffle(temp_stimuli_per_round)
        all_stimuli.extend(temp_stimuli_per_round)

    stimuli_count = len(all_stimuli)
    print('Total stimuli segments: ', stimuli_count, ', rounds: ', total_rounds)

    # randomize
    shuffle(all_stimuli)

    # separate non-consecutive stimuli
    stimuli_with_acceptable_consecutive = [stimulus for stimulus in all_stimuli if
                                           stimulus not in NON_CONSECUTIVE_STIMULI]
    stimuli_with_unacceptable_consecutive = [stimulus for stimulus in all_stimuli if
                                             stimulus in NON_CONSECUTIVE_STIMULI]
    # new_indices_for_unacceptable_consecutive_stimuli = sample(
    #     range(0, len(stimuli_with_acceptable_consecutive), 2),
    #     len(stimuli_with_unacceptable_consecutive))
    len_acceptable_consecutive = len(stimuli_with_acceptable_consecutive)
    len_unacceptable_consecutive = len(stimuli_with_unacceptable_consecutive)
    # append to start and end
    new_indices_for_unacceptable_consecutive_stimuli = sample(
        range(0, len_unacceptable_consecutive // 2 + 1), len_unacceptable_consecutive // 2)
    new_indices_for_unacceptable_consecutive_stimuli.extend(sample(range(
        len_acceptable_consecutive - len_unacceptable_consecutive + len_unacceptable_consecutive // 2,
        len_acceptable_consecutive + 1),
        len_unacceptable_consecutive - len_unacceptable_consecutive // 2))
    new_indices_for_unacceptable_consecutive_stimuli.sort(reverse=True)
    # update indices of unacceptable consecutive stimuli
    all_stimuli = stimuli_with_acceptable_consecutive
    for new_index in new_indices_for_unacceptable_consecutive_stimuli:
        all_stimuli.insert(new_index, stimuli_with_unacceptable_consecutive.pop(0))

    # print(all_stimuli, len(all_stimuli))

    stimuli_types = [stimulus for stimulus in all_stimuli for i in
                     range(len(STIMULI_IMAGE_ID_MAPPING[stimulus]))]
    print(
        f'shape count: {len(stimuli_types)}, duration: {IMAGE_DURATION_MS * len(stimuli_types) / 1000}')
    stimuli_ids = list(range(1, len(stimuli_types) + 1))
    image_ids = [image_id for stimulus in all_stimuli for image_id in
                 STIMULI_IMAGE_ID_MAPPING[stimulus]]
    stimuli_csv_data = {'stimuli_type': stimuli_types, 'stimuli_id': stimuli_ids,
                        'image_id': image_ids}

    pd.DataFrame(data=stimuli_csv_data).to_csv(csv_file_name, mode='w', index=False)
    print('Generated new stimuli csv: ', csv_file_name)

# generate_new_stimuli_csv('stimuli/tmp.csv')
