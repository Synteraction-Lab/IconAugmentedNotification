# coding=utf-8

import utilities
from random import shuffle
from pynput import keyboard

DEVICE_IP = '192.168.43.67'
# DEVICE_IP = '192.168.18.17'

DISPLAY_URL = 'http://' + DEVICE_IP + ':8080/displays/10/'

current_index = -1


def get_next_icon():
    global current_index

    if current_index == -1:
        shuffle(ALL_ICONS)

    current_index += 1

    if current_index < len(ALL_ICONS):
        return ALL_ICONS[current_index]
    else:
        return None


current_icon = None


def send_next_icon():
    global current_icon

    if current_icon is None:
        current_icon = get_next_icon()
        if current_icon is None:
            utilities.send_request(DISPLAY_URL, {"subheading": ""})
            return False
        else:
            icon_copy = current_icon.copy()
            icon_copy.update({"subheading": "   ? "})
            utilities.send_request(DISPLAY_URL, icon_copy)
            return True
    else:
        utilities.send_request(DISPLAY_URL, current_icon)
        current_icon = None
        return True


def on_press(key):
    # print("Key: ", key)
    if key == keyboard.Key.down:
        return send_next_icon()
        # return False  # stop listener


ALL_ICONS = [
    {
        "subheading": "  WhatsApp",
        "image": "#FF00FF7D img_whatsapp"
    },
    {
        "subheading": "  Birthday",
        "image": "#FF00FF7D img_birthday"
    },
    {
        "subheading": "  Alarm",
        "image": "#FF00FF7D alarm"
    },
    # {
    #     "subheading": "  Meet (at location)",
    #     "image": "#FF00FF7D img_meet"
    # },
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
        "image": "#FF00FF7D img_credit_card2"
    },
    {
        "subheading": "  PIN (transaction)",
        "image": "#FF00FF7D img_pin"
    },
    {
        "subheading": "  Leave",
        "image": "#FF00FF7D img_leave"
    },

    {
        "subheading": "  Meeting",
        "image": "#FF00FF7D img_meeting"
    },
    {
        "subheading": "  Presentation",
        "image": "#FF00FF7D img_presentation2"
    },
    {
        "subheading": "  Doctor (appointment)",
        "image": "#FF00FF7D img_doctor"
    },
    {
        "subheading": "  Cleaning",
        "image": "#FF00FF7D img_cleaning"
    },
    {
        "subheading": "  Delivery",
        "image": "#FF00FF7D img_delivery"
    },
    {
        "subheading": "  Call",
        "image": "#FF00FF7D call"
    },
    {
        "subheading": "  Email",
        "image": "#FF00FF7D gmail"
    },
    {
        "subheading": "  Battery (low)",
        "image": "#FF00FF7D battery_low"
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
        "subheading": "  Movie",
        "image": "#FF00FF7D img_movie"
    },
    {
        "subheading": "  Ticket",
        "image": "#FF00FF7D img_ticket"
    },
    {
        "subheading": "  Car (arrival)",
        "image": "#FF00FF7D img_taxi"
    },
    {
        "subheading": "  Bus (arrival)",
        "image": "#FF00FF7D img_bus_departure"
    },
    {
        "subheading": "  Flight",
        "image": "#FF00FF7D img_plane"
    },
    {
        "subheading": "  Exercise",
        "image": "#FF00FF7D img_exercise_gym"
    },
    {
        "subheading": "  Yoga",
        "image": "#FF00FF7D img_yoga"
    },
    {
        "subheading": "  Standup",
        "image": "#FF00FF7D img_standup"
    },
    {
        "subheading": "  Cycling",
        "image": "#FF00FF7D img_cycling"
    },
    {
        "subheading": "  Buy (Add to cart)",
        "image": "#FF00FF7D img_add_shopping"
    },

    {
        "subheading": "  Send",
        "image": "#FF00FF7D img_send"
    },
    {
        "subheading": "  Reply",
        "image": "#FF00FF7D img_reply"
    },
    {
        "subheading": "  Forward",
        "image": "#FF00FF7D img_forward"
    },
    # {
    #     "subheading": "  Identity card",
    #     "image": "#FF00FF7D img_id_card"
    # },
    {
        "subheading": "  License (driving)",
        "image": "#FF00FF7D img_licence"
    },
    {
        "subheading": "  Rental (pay)",
        "image": "#FF00FF7D img_pay_rent2"
    },
    {
        "subheading": "  Pay (cash)",
        "image": "#FF00FF7D img_pay_cash2"
    },
    {
        "subheading": "  Pay (mobile)",
        "image": "#FF00FF7D img_pay_mobile"
    },
    {
        "subheading": "  Backup (computer)",
        "image": "#FF00FF7D img_backup_computer3"
    },
    {
        "subheading": "  Download",
        "image": "#FF00FF7D img_download"
    },

    {
        "subheading": "  Delete",
        "image": "#FF00FF7D img_delete"
    },
    {
        "subheading": "  Take (photo)",
        "image": "#FF00FF7D img_take_photo"
    },
    # {
    #     "subheading": "  Sync (photos)",
    #     "image": "#FF00FF7D img_sync_photos"
    # },
    # {
    #     "subheading": "  Order (online)",
    #     "image": "#FF00FF7D img_order_online"
    # },
    # {
    #     "subheading": "  Top-up (cash)",
    #     "image": "#FF00FF7D img_topup_cash"
    # },
]

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()  # remove if main thread is polling self.keys