import pywhatkit as kit
from datetime import datetime
from plyer import notification
import time
from tkinter import *
from threading import Thread


class info:
    def __init__(self, name, ph_no, birth_date):
        # taking the information
        self.phone_number = ph_no
        self.name = name
        self.birth_date = birth_date

    def date_diff_in_seconds(self):
        # Specified birth_day date
        date1 = datetime.strptime(self.birth_date, '%Y-%m-%d %H:%M:%S')
        # Current date
        date2 = datetime.now()
        timedelta = date1 - date2
        time_in_seconds = timedelta.days * 24 * 3600 + timedelta.seconds
        return time_in_seconds

    def for_notification(self):  # this block is for notification
        count = 0
        while count < 1:
            notification.notify(
                title="Birthday Notification",
                message=f"tomorrow your friend {self.name} birthday",
                timeout=1
            )
            count += 1
            time.sleep(10)

    # for sending whatsapp message at 12 o clock night
    def whatsapp(self):
        kit.sendwhatmsg(self.phone_number, message=f"happy birthday {self.name}", time_hour=9, time_min=56,
                        wait_time=20)


# all my friends name, whatsapp_number and their birth_day date
prakash = info("prakash", "+916281971648", '2021-04-04 00:00:00')
aravind_reddy = info("aravind", "+916281289158", '2020-11-22 00:00:00')
rama_swamy = info("ramaswamy", "+919445421390", '2020-12-06 00:00:00')
rohit = info("rohit", "+918465947182", '2021-01-05 00:00:00')
krishna_chaithanya = info("krishna", "+917396184165", "2021-01-22 00:00:00")


def gui():
    bg = '#FFFF99'
    fg = '#2b2b2b'
    root = Tk()
    root.geometry('700x400')
    root.title('Birth_day Time')
    root.configure(bg=bg)

    Label(root, text="Your friends and their birth_dates", font=("", 30), bg=bg, fg=fg).place(x=10, y=20)
    Label(root, text="prakash - 4th april", font=("", 18), bg=bg, fg=fg).place(x=20, y=80)
    Label(root, text="aravind_reddy - 2nd december", font=("", 18), bg=bg, fg=fg).place(x=20, y=120)
    Label(root, text="ramaswany - 6th december", font=("", 18), bg=bg, fg=fg).place(x=20, y=160)
    Label(root, text="rohit - 5th january", font=("", 18), bg=bg, fg=fg).place(x=20, y=200)
    Label(root, text="krishna - 22nd january", font=("", 18), bg=bg, fg=fg).place(x=20, y=240)

    root.mainloop()


def all_friends(friend_name):
    if 0 < friend_name.date_diff_in_seconds() < 7 * 3600:
        Thread(target=friend_name.for_notification).start()
        Thread(target=friend_name.whatsapp).start()


def sample():  # calling the functions to send message
    all_friends(prakash)
    all_friends(aravind_reddy)
    all_friends(rama_swamy)
    all_friends(rohit)
    all_friends(krishna_chaithanya)


if __name__ == '__main__':
    Thread(target=gui).start()
    Thread(target=sample).start()
