# coding=utf-8

# command format: python3 txt_to_csv.py file_name.txt


def get_empty_notification(type, duration):
    return {
        "type": type,
        "id": -1,
        "duration": duration
    }


# notification_data: { "id": <id>, "title": <title>, "message": <message> , "iconColor": <#color> , "iconName":  <app_icon>, "appName": <app_name> }
def get_full_notification(type, notification_data, when, duration):
    return {
        "type": type,
        "id": notification_data["id"],
        "title": notification_data["title"],
        "message": notification_data["message"],
        "appName": notification_data["appName"],
        "when": when,
        "duration": duration,
        "smallIcon": "{} {}".format(notification_data["iconColor"], notification_data["iconName"])
    }


# icon_data: { "id": <id>, "iconColor": <#color> , "iconName":  <app_icon>, "appName": <app_name> }
def get_icon_notification(type, icon_data, when, duration):
    return {
        "type": type,
        "id": icon_data["id"],
        "appName": icon_data["appName"],
        "when": when,
        "duration": duration,
        "smallIcon": "{} {}".format(icon_data["iconColor"], icon_data["iconName"])
    }


# title_data: { "id": <id>, "title"": <title> }
def get_title_notification(type, title_data, when, duration):
    return {
        "type": type,
        "id": title_data["id"],
        "title": title_data["title"],
        "when": when,
        "duration": duration,
    }


# message_data: { "id": <id>, "message": <message_content> }
def get_message_notification(type, message_data, when, duration):
    return {
        "type": type,
        "id": message_data["id"],
        "message": message_data["message"],
        "when": when,
        "duration": duration,
    }


def get_updated_notification_with_reading_passage(notification, notification_config,
                                                  reading_question, when):
    # update when to show notification
    notification.update({"when": when})

    # append the question to the notification_config
    notification_config = "{},{},{},".format(notification_config,
                                             reading_question.get('Header', ''),
                                             reading_question.get('Passage').replace(",", "|"))
    notification.update({"config": notification_config})

    return notification


def get_updated_subsequent_notification(notification, notification_config, when):
    # update when to show notification
    notification.update({"when": when})

    # update config to support no refresh
    notification_config = "{},".format(
        notification_config.replace("PROGRESSIVE_WITH_DISPLAY", "PROGRESSIVE_WITH_NO_REFRESH"))
    notification.update({"config": notification_config})

    return notification


def get_mcq_display_data(question, options, selected=""):
    return {
        "heading": "{}".format(question),
        "content": "{}|{}|{}|{}|{}".format(
            options[0],
            options[1],
            options[2],
            options[3],
            selected),
        "config": "MCQ_CHOICES"
    }


def get_display_data_without_refresh(heading, subheading, content=""):
    return {
        "heading": heading,
        "subheading": subheading,
        "content": content,
        "config": "NO_REFRESH"
    }


def get_calibration_display_data():
    return {
        "subheading": "AA                                                          BB                                                          CC "
                      "\n\n\n"
                      "MM                                                         O                                                           PP "
                      "\n\n\n"
                      "XX                                                          YY                                                          ZZ"
    }


def get_center_point_display_data():
    return {
        "subheading": "\n\n\n                                                                LOL"
    }


def get_dummy_display_data():
    return {
        "subheading": "Lorem ipsum is a pseudo-Latin text used in web design, typography, layout, "
                      "and printing in place of English to emphasise design elements over content. "
                      "It's also called placeholder (or filler) text. It's a convenient tool for mock-ups. "
                      "It helps to outline the visual elements of a document or presentation, "
                      "eg typography, font, or layout. Lorem ipsum is mostly a part of a Latin text "
                      "by the classical author and philosopher Cicero. Its words and letters have been "
                      "changed by addition or removal, so to deliberately render its content nonsensical;"
                      " it's not genuine, correct, or comprehensible Latin anymore."
    }


def get_mcq_reading_question_display_data(reading_question, question_number, selected=""):
    return get_mcq_display_data(
        reading_question["Question_{}".format(question_number)],
        [
            reading_question["Option1_{}".format(question_number)],
            reading_question["Option2_{}".format(question_number)],
            reading_question["Option3_{}".format(question_number)],
            reading_question["Option4_{}".format(question_number)],
        ],
        selected
    )


def get_notification_reading_question_display_data(notification_question, selected=""):
    return get_mcq_display_data(
        notification_question["Question"],
        [
            notification_question["Option1"],
            notification_question["Option2"],
            notification_question["Option3"],
            notification_question["Option4"]
        ],
        selected
    )
