# coding=utf-8

import participant_config
import device_config
import utilities

from pynput import keyboard
from random import shuffle

DEVICE_IP = device_config.get_device_ip()

DISPLAY_URL = 'http://' + DEVICE_IP + ':8080/displays/10/'

current_index = -1

participant = 'p0'

MAX_RETRY_ATTEMPT = 3


def get_next_icon():
    global current_index

    if current_index == -1:
        shuffle(ALL_ICONS)

    current_index += 1

    if current_index < len(ALL_ICONS):
        return ALL_ICONS[current_index].copy()
    else:
        return None


def send_until_success(display_data):
    attempt = 0
    success = False
    while not success and attempt < MAX_RETRY_ATTEMPT:
        success = utilities.send_request(DISPLAY_URL, display_data)
        attempt += 1

        if not success and attempt < MAX_RETRY_ATTEMPT:
            utilities.sleep_seconds(0.5)
    return success


current_icon = None


def send_next_icon():
    global current_icon

    if current_icon is None:
        current_icon = get_next_icon()
        if current_icon is None:
            send_until_success({"subheading": ""})
            return False
        else:
            # update icon
            icon_info = current_icon.get("image").split()  # <color> <icon_name>
            updated_icon_info = f'{icon_info[0]} {icon_info[1]}{participant_config.get_icon_suffix(participant, icon_info[1])}'
            current_icon["image"] = updated_icon_info

            icon_copy = current_icon.copy()
            icon_copy["subheading"] = "   ? "
            send_until_success(icon_copy)
            return True
    else:
        send_until_success(current_icon)
        current_icon = None
        return True


def on_press(key):
    # print("Key: ", key)
    if key == keyboard.Key.down:
        return send_next_icon()
        # return False  # stop listener


ALL_ICONS = [
    # {
    #     "subheading": "  Message",
    #     "image": "#FF00FF7D img_message"
    # },
    # {
    #     "subheading": "  Meet (at location)",
    #     "image": "#FF00FF7D img_meet"
    # },
    # {
    #     "subheading": "  PIN (transaction)",
    #     "image": "#FF00FF7D img_pin"
    # },
    # {
    #     "subheading": "  Send",
    #     "image": "#FF00FF7D img_send"
    # },
    # {
    #     "subheading": "  Forward",
    #     "image": "#FF00FF7D img_forward"
    # },
    # {
    #     "subheading": "  Cleaning",
    #     "image": "#FF00FF7D img_cleaning"
    # },
    # {
    #     "subheading": "  Yoga",
    #     "image": "#FF00FF7D img_yoga"
    # },
    # {
    #     "subheading": "  Cycling",
    #     "image": "#FF00FF7D img_cycling"
    # },
    # {
    #     "subheading": "  Buy (Add to cart)",
    #     "image": "#FF00FF7D img_buy"
    # },
    # {
    #     "subheading": "  Ticket",
    #     "image": "#FF00FF7D img_ticket"
    # },
    # {
    #     "subheading": "  Pay (mobile)",
    #     "image": "#FF00FF7D img_pay_mobile"
    # },
    # {
    #     "subheading": "  Identity card",
    #     "image": "#FF00FF7D img_id_card"
    # },
    # {
    #     "subheading": "  Delete",
    #     "image": "#FF00FF7D img_delete"
    # },

    {
        "subheading": "  Birthday",
        "image": "#FF00FF7D img_birthday"
    },
    {
        "subheading": "  Alarm",
        "image": "#FF00FF7D img_alarm"
    },
    {
        "subheading": "  Meeting",
        "image": "#FF00FF7D img_meeting"
    },
    {
        "subheading": "  Lunch",
        "image": "#FF00FF7D img_lunch"
    },
    {
        "subheading": "  Coffee",
        "image": "#FF00FF7D img_coffee"
    },
    {
        "subheading": "  Milk and eggs",
        "image": "#FF00FF7D img_milk_eggs"
    },
    {
        "subheading": "  Credit card",
        "image": "#FF00FF7D img_credit_card"
    },
    {
        "subheading": "  Delivery",
        "image": "#FF00FF7D img_delivery"
    },
    {
        "subheading": "  Email",
        "image": "#FF00FF7D img_email"
    },
    {
        "subheading": "  Reply",
        "image": "#FF00FF7D img_reply"
    },

    {
        "subheading": "  Leave",
        "image": "#FF00FF7D img_leave"
    },
    {
        "subheading": "  Visitor",
        "image": "#FF00FF7D img_visitor"
    },
    {
        "subheading": "  Presentation",
        "image": "#FF00FF7D img_presentation"
    },
    {
        "subheading": "  Doctor (appointment)",
        "image": "#FF00FF7D img_doctor"
    },
    {
        "subheading": "  Exercise",
        "image": "#FF00FF7D img_exercise"
    },
    {
        "subheading": "  Standup",
        "image": "#FF00FF7D img_standup"
    },
    {
        "subheading": "  Swimming",
        "image": "#FF00FF7D img_swimming"
    },
    {
        "subheading": "  Take (photo)",
        "image": "#FF00FF7D img_take_photo"
    },
    {
        "subheading": "  Sync (photos)",
        "image": "#FF00FF7D img_sync_photos"
    },
    {
        "subheading": "  Download",
        "image": "#FF00FF7D img_download"
    },

    {
        "subheading": "  Order (online)",
        "image": "#FF00FF7D img_order_online"
    },
    {
        "subheading": "  Call",
        "image": "#FF00FF7D img_call"
    },
    {
        "subheading": "  Movie",
        "image": "#FF00FF7D img_movie"
    },
    {
        "subheading": "  Valentine's day",
        "image": "#FF00FF7D img_valentine_day"
    },
    {
        "subheading": "  Mother's day",
        "image": "#FF00FF7D img_mom_day"
    },
    {
        "subheading": "  Battery (low)",
        "image": "#FF00FF7D img_battery_low"
    },
    {
        "subheading": "  Car (arrival)",
        "image": "#FF00FF7D img_car"
    },
    {
        "subheading": "  Bus (arrival)",
        "image": "#FF00FF7D img_bus"
    },
    {
        "subheading": "  Flight",
        "image": "#FF00FF7D img_flight"
    },
    {
        "subheading": "  Top-up (cash)",
        "image": "#FF00FF7D img_topup_cash"
    },

    {
        "subheading": "  Rental (pay)",
        "image": "#FF00FF7D img_pay_rent"
    },
    {
        "subheading": "  Pay (cash)",
        "image": "#FF00FF7D img_pay_cash"
    },
    {
        "subheading": "  License (driving)",
        "image": "#FF00FF7D img_licence"
    },
    {
        "subheading": "  Backup (computer)",
        "image": "#FF00FF7D img_backup_computer"
    },
]

_participant = input("Participant id (e.g. p0) ? ")
if _participant == '':
    _participant = 'p0'
participant = _participant

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()  # remove if main thread is polling self.keys
