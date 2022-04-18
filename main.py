import sys
import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
import shutil

source_path = f"C:/Users/iloke/Downloads/"
imgs_path = f"C:/Users/iloke/Downloads/Pictures/"
pdf_path = f"C:/Users/iloke/Downloads/PDF/"
zip_path = f"C:/Users/iloke/Downloads/Zip/"
unsplash_path =  f"C:/Users/iloke/Downloads/Unsplash"
word_path = f"C:/Users/iloke/Downloads/WordDocs/"
excel_path = f"C:/Users/iloke/Downloads/ExcelDocs/"

list = os.listdir(source_path)

class Event(FileSystemEventHandler):
    def dispatch(self, event):
        time.sleep(5)
        for file_name in os.listdir(source_path):
            source = source_path + file_name
            img_folder = imgs_path + file_name
            pdf_folder = pdf_path + file_name
            zip_folder = zip_path + file_name
            unsplash_folder = zip_path + file_name
            word_folder = word_path + file_name
            excel_folder = excel_path + file_name
            
            if ".jpg" in file_name or ".png" in file_name or ".jpeg" in file_name:
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