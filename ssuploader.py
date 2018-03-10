#!/usr/bin/env python
# -*- coding: utf-8 -*-

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from imgurpython import ImgurClient

import os
import time

target_dir = "./"

client_id = your id
client_secret = your secret

client = ImgurClient(client_id, client_secret)

def getext(filename):
    return os.path.splitext(filename)[-1].lower()

class ChangeHandler(FileSystemEventHandler):
    def on_created(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        if getext(event.src_path) in ('.png'):
          image = client.upload_from_path(filename, config=None, anon=False)
          print( image['link'] )
          
          
if __name__ in '__main__':
    while 1:
        event_handler = ChangeHandler()
        observer = Observer()
        observer.schedule(event_handler, target_dir, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
