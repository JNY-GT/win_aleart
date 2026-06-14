from winotify import Notification


def send_notification(title, message):

    toast = Notification(
        app_id="Weather Alert",
        title=title,
        msg=message
    )

    toast.show()