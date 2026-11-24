import json
import time

def load_content (file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content  = json.load(f)
            return content
    except Exception as e:
        print("Errno :> ", e)
        return -1

def wait(seconds=1):
    try:
        seconds = float(seconds)
    except:
        seconds = 1
    time.sleep(seconds)