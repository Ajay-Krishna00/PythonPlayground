import time
import psutil
from plyer import notification

def check_battery():
    battery = psutil.sensors_battery()
    battery_percent = battery.percent
    battery_plugged = battery.power_plugged

    if battery_plugged and battery_percent == 100:
        notification.notify(
            title="Battery Full",
            message="Battery is fully charged.",
            timeout=10
        )
    elif not battery_plugged and battery_percent <= 30:
        notification.notify(
            title="Battery Low",
            message=f"Battery is {battery_percent}%. Please plug in the charger.",
            timeout=10
        )
    elif not battery_plugged and battery_percent % 10 == 0:
        notification.notify(
            title="Battery Status",
            message=f"Battery is {battery_percent}%",
            timeout=8
        )

if __name__ == "__main__":
    while True:
        check_battery()
        time.sleep(60)  