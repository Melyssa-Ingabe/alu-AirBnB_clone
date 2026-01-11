#!/usr/bin/python3
from models.engine.tmp_file_storage import *
from models.engine.tmp_file_storage import FileStorage

class FileStorageSub(FileStorage):
    def reload(self):
        pass

try:
    fs = FileStorageSub()
    fs.reload()
    print("OK")
except Exception as e:
    print(f"Error: {e}")
