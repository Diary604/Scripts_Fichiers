import sys
import time
import os
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import mimetypes

class FileCreateHandler(FileSystemEventHandler):
    def on_created(self, event):
        
        if event.is_directory:#is_directory: bool = field(default=False, init=False)
            return

        filepath = event.src_path
        filename = os.path.basename(filepath)
        file_type, encoding = mimetypes.guess_type(filepath)
        self.element_list = os.listdir()

        print(f"Filename : {filename} ")
        print(f"Directory: {filepath}")
        print(f"Type: {file_type}")
        print(f"list_dir : {self.element_list}")
        print("------------------------------")
    def create_folder(self):
        self.element_list

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')

    path = sys.argv[1] if len(sys.argv) > 1 else "."
    
    event_handler = FileCreateHandler() 
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    
    print(f"Surveillance du dossier : {path}")
    observer.start()
    
    try:
        while True:
            observer.join(1)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()
