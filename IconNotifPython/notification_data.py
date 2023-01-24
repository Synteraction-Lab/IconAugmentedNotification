# coding=utf-8


import utilities
from random import shuffle

index_training_data = -1

index_testing_data = -1
order_testing_data = []

NOTIFICATION_TYPE_NONE = 'none'
NOTIFICATION_TYPE_TEXT_LONG = 'text_long'
NOTIFICATION_TYPE_IMAGE_SHORT = 'image_short'
NOTIFICATION_TYPE_TEXT_SHORT = 'text_short'
NOTIFICATION_TYPE_IMAGE_LONG = 'image_long'


def is_no_notification(type):
    return type == NOTIFICATION_TYPE_NONE


def get_all_testing_notifications():
    return NOTIFICATION_TESTING_DATA.copy()


def shuffle_data():
    print("shuffle_data")
    shuffle(NOTIFICATION_TRAINING_IMAGE_DATA)
    shuffle(NOTIFICATION_TRAINING_TEXT_SHORT_DATA)


def get_next_notification_training_data(data_type):
    global index_training_data

    if data_type == NOTIFICATION_TYPE_IMAGE_SHORT:
        data_list = NOTIFICATION_TRAINING_IMAGE_DATA
    elif data_type == NOTIFICATION_TYPE_TEXT_SHORT:
        data_list = NOTIFICATION_TRAINING_TEXT_SHORT_DATA
    else:
        return NOTIFICATION_EMPTY

    index_training_data += 1
    if index_training_data >= len(data_list):
        index_training_data = 0

    return data_list[index_training_data].copy()


SEQUENCE_FILE_NOTIFICATION = "_sequence_testing_notifications.json"


def is_supported_type(data_type):
    if data_type == NOTIFICATION_TYPE_TEXT_LONG or \
            data_type == NOTIFICATION_TYPE_IMAGE_SHORT or \
            data_type == NOTIFICATION_TYPE_TEXT_SHORT or \
            data_type == NOTIFICATION_TYPE_IMAGE_LONG:
        return True

    return False


# data_type = DATA_TYPE_TEXT -> text, DATA_TYPE_IMAGE -> image
def get_next_notification_testing_data(data_type):
    global index_testing_data
    global order_testing_data

    if not is_supported_type(data_type):
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

    # FIXME: this logic is wrong
    while data_list[order_testing_data[index_testing_data]].get(data_type) is None:
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

NOTIFICATION_TRAINING_IMAGE_DATA = [
    {
        "id": 21,
        "subheading": "  Mary",
        "image": "#FF00FF7D img_call"
    },
    {
        "id": 22,
        "subheading": "  8 am",
        "image": "#FF00FF7D img_alarm"
    },
    {
        "id": 23,
        "subheading": "  10%",
        "image": "#FF00FF7D img_battery_low"
    }
]

NOTIFICATION_TRAINING_TEXT_SHORT_DATA = [
    {
        "id": 1,
        "subheading": "Swimming   5 pm"
    },
    {
        "id": 2,
        "subheading": "Visit   museum"
    },
    {
        "id": 3,
        "subheading": "Deposit   SGD 10"
    }
]

# count = 19
NOTIFICATION_TESTING_DATA = [
    {
        'text_short': {
            "id": 301,
            "subheading": "Meeting   4 pm"
        },
        # 'image_short': {
        #     "id": 301,
        #     "subheading": "  4 pm",
        #     "image": "#FF00FF7D img_meeting"
        # },
    },
    {
        'text_short': {
            "id": 303,
            "subheading": "Lunch   Lee"
        },
        # 'image_short': {
        #     "id": 303,
        #     "subheading": "  Lee",
        #     "image": "#FF00FF7D img_lunch"
        # },
    },
    {
        'text_short': {
            "id": 309,
            "subheading": "Pay   SGD 200"
        },
        # 'image_short': {
        #     "id": 309,
        #     "subheading": "  SGD 200",
        #     "image": "#FF00FF7D img_pay_cash"
        # },
    },
    {
        'text_short': {
            "id": 312,
            "subheading": "Presentation   12 pm"
        },
        # 'image_short': {
        #     "id": 312,
        #     "subheading": "  12 pm",
        #     "image": "#FF00FF7D img_presentation"
        # },
    },
    {
        'text_short': {
            "id": 317,
            "subheading": "Reply   Alex"
        },
        # 'image_short': {
        #     "id": 317,
        #     "subheading": "  Alex",
        #     "image": "#FF00FF7D img_reply"
        # },
    },
    {
        'text_short': {
            "id": 321,
            "subheading": "Movie   Sunday"
        },
        # 'image_short': {
        #     "id": 321,
        #     "subheading": "  Sunday",
        #     "image": "#FF00FF7D img_movie"
        # },
    },

    {
        'image_short': {
            "id": 307,
            "subheading": "  5 min",
            "image": "#FF00FF7D img_car"
        },
        # 'text_short': {
        #     "id": 307,
        #     "subheading": "Car   5 min"
        # },
    },
    {
        'image_short': {
            "id": 304,
            "subheading": "  John",
            "image": "#FF00FF7D img_birthday"
        },
        # 'text_short': {
        #     "id": 304,
        #     "subheading": "Birthday   John"
        # },
    },
    {
        'image_short': {
            "id": 308,
            "subheading": "  3 d",
            "image": "#FF00FF7D img_delivery"
        },
        # 'text_short': {
        #     "id": 308,
        #     "subheading": "Delivery   3 d"
        # },
    },
    {
        'image_short': {
            "id": 315,
            "subheading": "  40 min",
            "image": "#FF00FF7D img_exercise"
        },
        # 'text_short': {
        #     "id": 315,
        #     "subheading": "Exercise   40 min"
        # },
    },
    {
        'image_short': {
            "id": 316,
            "subheading": "  status",
            "image": "#FF00FF7D img_flight"
        },
        # 'text_short': {
        #     "id": 316,
        #     "subheading": "Flight   status"
        # },
    },
    {
        'image_short': {
            "id": 310,
            "subheading": "  today",
            "image": "#FF00FF7D img_credit_card"
        },
        # 'text_short': {
        #     "id": 310,
        #     "subheading": "Credit card   today"
        # },
    },

    {
        'text_long': {
            "id": 330,
            "subheading": "Valentine's day   2 d"
        },
        # 'image_long': {
        #     "id": 330,
        #     "subheading": "  2 d",
        #     "image": "#FF00FF7D img_valentine_day"
        # },
    },
    {
        'text_long': {
            "id": 331,
            "subheading": "Sync photos   Friday"
        },
        # 'image_long': {
        #     "id": 331,
        #     "subheading": "  Friday",
        #     "image": "#FF00FF7D img_sync_photos"
        # },
    },
    {
        'text_long': {
            "id": 332,
            "subheading": "Bus departure   25 min"
        },
        # 'image_long': {
        #     "id": 332,
        #     "subheading": "  25 min",
        #     "image": "#FF00FF7D img_bus"
        # },
    },
    {
        'text_long': {
            "id": 333,
            "subheading": "Order online   Amazon"
        },
        # 'image_long': {
        #     "id": 333,
        #     "subheading": "  Amazon",
        #     "image": "#FF00FF7D img_order_online"
        # },
    },
    {
        'text_long': {
            "id": 334,
            "subheading": "Apply leave   vacation"
        },
        # 'image_long': {
        #     "id": 334,
        #     "subheading": "  vacation",
        #     "image": "#FF00FF7D img_leave"
        # },
    },
    {
        'text_long': {
            "id": 313,
            "subheading": "Pay rental   Monday"
        },
        # 'image_long': {
        #     "id": 313,
        #     "subheading": "  Monday",
        #     "image": "#FF00FF7D img_pay_rent"
        # },
    },

    {
        'image_long': {
            "id": 301,
            "subheading": "  2 hrs",
            "image": "#FF00FF7D img_doctor"
        },
        # 'text_long': {
        #     "id": 301,
        #     "subheading": "Doctor's appointment   2 hrs"
        # },
    },
    {
        'image_long': {
            "id": 320,
            "subheading": "  tonight",
            "image": "#FF00FF7D img_backup_computer"
        },
        # 'text_long': {
        #     "id": 320,
        #     "subheading": "Backup computer   tonight"
        # },
    },
    {
        'image_long': {
            "id": 318,
            "subheading": "  renew",
            "image": "#FF00FF7D img_licence"
        },
        # 'text_long': {
        #     "id": 318,
        #     "subheading": "Driving license   renew"
        # },
    },
    {
        'image_long': {
            "id": 314,
            "subheading": "  FairPrice",
            "image": "#FF00FF7D img_milk_eggs"
        },
        # 'text_long': {
        #     "id": 314,
        #     "subheading": "Milk and eggs   FairPrice"
        # },
    },
    {
        'image_long': {
            "id": 335,
            "subheading": "  EzLink",
            "image": "#FF00FF7D img_topup_cash"
        },
        # 'text_long': {
        #     "id": 335,
        #     "subheading": "Top-up cash   EzLink"
        # },
    },
    {
        'image_long': {
            "id": 305,
            "subheading": "  7 d",
            "image": "#FF00FF7D img_mom_day"
        },
        # 'text_long': {
        #     "id": 305,
        #     "subheading": "Mother's day   7 d"
        # },
    },

    # {
    #     'text_short': {
    #         "id": 324,
    #         "subheading": "Download   e-bill"
    #     },
    #     'image_short': {
    #         "id": 324,
    #         "subheading": "  e-bill",
    #         "image": "#FF00FF7D img_download"
    #     },
    # },
    # {
    #     'text_short': {
    #         "id": 325,
    #         "subheading": "Coffee   Sam"
    #     },
    #     'image_short': {
    #         "id": 324,
    #         "subheading": "  Sam",
    #         "image": "#FF00FF7D img_coffee"
    #     },
    # },
    # {
    #     'text_short': {
    #         "id": 326,
    #         "subheading": "Email   agenda"
    #     },
    #     'image_short': {
    #         "id": 326,
    #         "subheading": "  agenda",
    #         "image": "#FF00FF7D img_email"
    #     },
    # },
    #
    # {
    #     'text_long': {
    #         "id": 327,
    #         "subheading": "Take photo   Zoo"
    #     },
    #     'image_long': {
    #         "id": 327,
    #         "subheading": "  Zoo",
    #         "image": "#FF00FF7D img_take_photo"
    #     },
    # },
    # {
    #     'text_long': {
    #         "id": 328,
    #         "subheading": "Visitor coming   1 month"
    #     },
    #     'image_long': {
    #         "id": 328,
    #         "subheading": "  1 month",
    #         "image": "#FF00FF7D img_visitor"
    #     },
    # },
    # {
    #     'text_long': {
    #         "id": 329,
    #         "subheading": "Stand up   stretch"
    #     },
    #     'image_long': {
    #         "id": 329,
    #         "subheading": "  stretch",
    #         "image": "#FF00FF7D img_standup"
    #     },
    # },
]
