import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source  = "main.txt"              # Add the path of you "Downloads" folder.
to_dir = "newfile.txt" #Create "Document_Files" folder in your Desktop and update the path accordingly.

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        os.rename(source, to_dir)
# Initialize Event Handler Class
event_handler = FileMovementHandler()

