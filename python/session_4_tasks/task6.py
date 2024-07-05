"""
Run this code (%battery and make notification)

"""

from pynotifier import Notification, NotificationClient
from pynotifier.backends import platform
import psutil

c = NotificationClient()

c.register_backend(platform.Backend())

battery = psutil.sensors_battery()
percent = battery.percent

print(percent)

c.notify_all(Notification(title="Battery Percentage", message=f"{str(percent)} %Percent Remaining", duration=10))

