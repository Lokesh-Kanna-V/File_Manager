import sys
import os
import time
import webbrowser
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
import shutil


def wait(sec):
    time.sleep(sec)


# Work Automation
# Google_dashboard = "https://workspace.google.com/dashboard"
Google_mail = "https://mail.google.com/mail/u/0/"
Google_calendar = "https://calendar.google.com"
# Google_chat = "https://mail.google.com/chat/u/0/#chat/welcome"
Google_drive = "https://drive.google.com/drive/u/0/folders/16RBo1CDsQqhzgsctJY6pZ03s1qW0cdhr"

comorin_login = input("Do you want to login to Comorin? (y/n): ")

if comorin_login == "y":
    print("Ok, Logging in")
    # webbrowser.open(Google_dashboard)
    # wait(2)
    webbrowser.open(Google_calendar)
    wait(2)
    webbrowser.open(Google_drive)
    wait(2)
    webbrowser.open(Google_mail)
    wait(2)
    # webbrowser.open(Google_chat)
    # wait(2)
    print("Logged in to Comorin Technologies")
else:
    print("Ok, Not Logging in")


source_path = f"C:/Users/iloke/Downloads/"
imgs_path = f"C:/Users/iloke/Downloads/Pictures/"
vids_path = f"C:/Users/iloke/Downloads/Videos/"
pdf_path = f"C:/Users/iloke/Downloads/PDF/"
zip_path = f"C:/Users/iloke/Downloads/Zip/"
unsplash_path = f"C:/Users/iloke/Downloads/Unsplash"
word_path = f"C:/Users/iloke/Downloads/WordDocs/"
excel_path = f"C:/Users/iloke/Downloads/ExcelDocs/"
powerpoint_path = f"C:/Users/iloke/Downloads/PowerPointDocs/"

list = os.listdir(source_path)


class Event(FileSystemEventHandler):
    def dispatch(self, event):
        time.sleep(5)
        for file_name in os.listdir(source_path):
            source = source_path + file_name
            img_folder = imgs_path + file_name
            vid_folder = vids_path + file_name
            pdf_folder = pdf_path + file_name
            zip_folder = zip_path + file_name
            unsplash_folder = zip_path + file_name
            word_folder = word_path + file_name
            excel_folder = excel_path + file_name
            powerpoint_folder = powerpoint_path + file_name

            if ".jpg" in file_name or ".png" in file_name or ".jpeg" in file_name or ".gif" in file_name:
                shutil.move(source, img_folder)
                print('Moved:', file_name, "to", img_folder)
            elif ".pdf" in file_name:
                shutil.move(source, pdf_folder)
                print('Moved:', file_name, "to", pdf_folder)
            elif ".zip" in file_name:
                shutil.move(source, zip_folder)
                print('Moved:', file_name, "to", zip_folder)
            elif "unsplash" in file_name:
                shutil.move(source, unsplash_folder)
                print('Moved:', file_name, "to", unsplash_folder)
            elif ".docx" in file_name:
                shutil.move(source, word_folder)
                print('Moved:', file_name, "to", word_folder)
            elif ".xlsx" in file_name:
                shutil.move(source, excel_folder)
                print('Moved:', file_name, "to", excel_folder)
            elif ".pptx" in file_name:
                shutil.move(source, powerpoint_folder)
                print('Moved:', file_name, "to", powerpoint_folder)
            elif ".webm" in file_name or ".mp4" in file_name or ".mov" in file_name or ".avi" in file_name or ".mkv" in file_name:
                shutil.move(source, powerpoint_folder)
                print('Moved:', file_name, "to", powerpoint_folder)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = "C:/Users/iloke/Downloads"
    event_handler = Event()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
