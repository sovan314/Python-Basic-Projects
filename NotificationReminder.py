import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "All Day Reminder",
            message = "Today I have to submit my Assignment and you have not completed it till now",
            timeout = 10

        )
        time.sleep(60)
