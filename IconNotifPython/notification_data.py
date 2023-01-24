# coding=utf-8


import utilities
from random import randint
from random import shuffle

index_training_data = -1

index_testing_data = -1
order_testing_data = []

NOTIFICATION_TYPE_TEXT = 'text'
NOTIFICATION_TYPE_IMAGE = 'image'


def get_all_testing_notifications():
    return NOTIFICATION_TESTING_DATA.copy()


def shuffle_data():
    print("shuffle_data")
    shuffle(NOTIFICATION_TRAINING_TEXT_DATA)
    shuffle(NOTIFICATION_TRAINING_IMAGE_DATA)


def get_next_notification_training_data(data_type):
    global index_training_data

    if data_type == NOTIFICATION_TYPE_TEXT:
        data_list = NOTIFICATION_TRAINING_TEXT_DATA
    elif data_type == NOTIFICATION_TYPE_IMAGE:
        data_list = NOTIFICATION_TRAINING_IMAGE_DATA
    else:
        return NOTIFICATION_EMPTY

    index_training_data += 1
    if index_training_data >= len(data_list):
        index_training_data = 0

    return data_list[index_training_data]


SEQUENCE_FILE_NOTIFICATION = "_sequence_testing_notifications.json"


# data_type = DATA_TYPE_TEXT -> text, DATA_TYPE_IMAGE -> image
def get_next_notification_testing_data(data_type):
    global index_testing_data
    global order_testing_data

    if data_type != NOTIFICATION_TYPE_TEXT and data_type != NOTIFICATION_TYPE_IMAGE:
        return NOTIFICATION_EMPTY

    data_list = NOTIFICATION_TESTING_DATA

    # at start check whether there is saved data
    if index_testing_data == -1:
        order_testing_data, index_testing_data = utilities.read_order_data(
            SEQUENCE_FILE_NOTIFICATION)
        if order_testing_data is None:
            print('\n Creating a new notification order\n')
            order_testing_data = list(range(len(data_list)))
            shuffle(order_testing_data)
            index_testing_data = -1
        else:
            print('\n Loading the previous notification order\n')

    index_testing_data += 1
    if index_testing_data >= len(data_list):
        index_testing_data = 0

    # save the current data
    utilities.save_order_data(SEQUENCE_FILE_NOTIFICATION, order_testing_data, index_testing_data)

    return data_list[order_testing_data[index_testing_data]][data_type].copy()


NOTIFICATION_EMPTY = {
    "id": 0,
    "subheading": ""
}

NOTIFICATION_TRAINING_TEXT_DATA = [
    {
        "id": 1,
        "subheading": "Email meeting agenda"
    },
    {
        "id": 2,
        "subheading": "Download e-bill online"
    },
    {
        "id": 3,
        "subheading": "Please approve the budget"
    }
]

NOTIFICATION_TRAINING_IMAGE_DATA = [
    {
        "id": 21,
        "subheading": " Mary",
        "image": "#FF00FF7D call"
    },
    {
        "id": 22,
        "subheading": " 8 am",
        "image": "#FF00FF7D alarm"
    },
    {
        "id": 23,
        "subheading": " 10%",
        "image": "#FF00FF7D battery_low"
    }
]

# count = 22
NOTIFICATION_TESTING_DATA = [
    {
        'text': {
            "id": 301,
            "subheading": "Meeting at 4 pm"
        },
        'image': {
            "id": 301,
            "subheading": "  4 pm",
            "image": "#FF00FF7D img_meeting"
        },
    },
    {
        'text': {
            "id": 302,
            "subheading": "Doctor's appointment in 2 hours"
        },
        'image': {
            "id": 301,
            "subheading": "  2 h",
            "image": "#FF00FF7D img_doctor"
        },
    },
    {
        'text': {
            "id": 303,
            "subheading": "Lunch with Lee at 1 pm"
        },
        'image': {
            "id": 303,
            "subheading": "  1 pm, Lee",
            "image": "#FF00FF7D img_lunch"
        },
    },
    {
        'text': {
            "id": 304,
            "subheading": "John's birthday tomorrow"
        },
        'image': {
            "id": 304,
            "subheading": "  1 d, John",
            "image": "#FF00FF7D img_birthday"
        },
    },
    {
        'text': {
            "id": 305,
            "subheading": "Mother's day next week"
        },
        'image': {
            "id": 305,
            "subheading": "  7 d",
            "image": "#FF00FF7D img_mom_day"
        },
    },
    # {
    #     'text': {
    #         "id": 306,
    #         "subheading": "A visitor coming Friday"
    #     },
    #     'image': {
    #         "id": 306,
    #         "subheading": "  Friday",
    #         "image": "#FF00FF7D img_visitor"
    #     },
    # },
    {
        'text': {
            "id": 307,
            "subheading": "Car is arriving in 5 minutes"
        },
        'image': {
            "id": 307,
            "subheading": "  5 min",
            "image": "#FF00FF7D img_taxi"
        },
    },

    {
        'text': {
            "id": 308,
            "subheading": "Delivery in 3 days"
        },
        'image': {
            "id": 308,
            "subheading": "  3 d",
            "image": "#FF00FF7D img_delivery"
        },
    },
    {
        'text': {
            "id": 309,
            "subheading": "Pay Eric SGD100"
        },
        'image': {
            "id": 309,
            "subheading": "  SGD100, Eric",
            "image": "#FF00FF7D img_pay_cash2"
        },
    },
    {
        'text': {
            "id": 310,
            "subheading": "Pay credit card bill today"
        },
        'image': {
            "id": 310,
            "subheading": "  today",
            "image": "#FF00FF7D img_credit_card2"
        },
    },
    # {
    #     'text': {
    #         "id": 311,
    #         "subheading": "Transaction of SGD20 complete"
    #     },
    #     'image': {
    #         "id": 311,
    #         "subheading": "  SGD20",
    #         "image": "#FF00FF7D img_transaction"
    #     },
    # },
    {
        'text': {
            "id": 312,
            "subheading": "Send the presentation by noon"
        },
        'image': {
            "id": 312,
            "subheading": "  12 pm",
            "image": "#FF00FF7D img_send_presentation2"
        },
    },
    {
        'text': {
            "id": 313,
            "subheading": "Pay rental on Monday"
        },
        'image': {
            "id": 313,
            "subheading": "  Monday",
            "image": "#FF00FF7D img_pay_rent2"
        },
    },
    {
        'text': {
            "id": 314,
            "subheading": "Buy milk and eggs tonight"
        },
        'image': {
            "id": 314,
            "subheading": "  tonight",
            "image": "#FF00FF7D img_shop_milk_eggs"
        },
    },
    {
        'text': {
            "id": 315,
            "subheading": "Exercise in 40 minutes"
        },
        'image': {
            "id": 315,
            "subheading": "  40 min",
            "image": "#FF00FF7D img_exercise_gym"
        },
    },
    {
        'text': {
            "id": 316,
            "subheading": "Check your flight status"
        },
        'image': {
            "id": 316,
            "subheading": "  status",
            "image": "#FF00FF7D img_plane"
        },
    },
    {
        'text': {
            "id": 317,
            "subheading": "Reply Alex now"
        },
        'image': {
            "id": 317,
            "subheading": "  Alex",
            "image": "#FF00FF7D img_reply"
        },
    },
    {
        'text': {
            "id": 318,
            "subheading": "Renew driving license"
        },
        'image': {
            "id": 318,
            "subheading": "  renew",
            "image": "#FF00FF7D img_licence"
        },
    },
    {
        'text': {
            "id": 319,
            "subheading": "Stand up and take a break"
        },
        'image': {
            "id": 319,
            "subheading": "  Break",
            "image": "#FF00FF7D img_standup"
        },
    },
    {
        'text': {
            "id": 320,
            "subheading": "Backup the computer tonight"
        },
        'image': {
            "id": 320,
            "subheading": "  tonight",
            "image": "#FF00FF7D img_backup_computer3"
        },
    },
    {
        'text': {
            "id": 321,
            "subheading": "Movie on Monday"
        },
        'image': {
            "id": 321,
            "subheading": "  Monday",
            "image": "#FF00FF7D img_movie"
        },
    },
    # {
    #     'text': {
    #         "id": 3,
    #         "subheading": ""
    #     },
    #     'image': {
    #         "id": 3,
    #         "subheading": "  ",
    #         "image": "#FF00FF7D img_visitor"
    #     },
    # },
]
