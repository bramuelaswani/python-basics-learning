from plyer import notification
import time

from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title='ALERT!!!',
            message='Hey Bramuel,Take a break, its been an hour!',
            timeout=15
        )
        time.sleep(3600)
