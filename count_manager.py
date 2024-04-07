import os

COUNT_FILE = "processing_count.txt"

def load_processing_count():
    global processing_count
    if os.path.exists(COUNT_FILE):
        with open(COUNT_FILE, "r") as file:
            processing_count = int(file.read().strip())
            print("Processing count loaded:", processing_count)
            return processing_count
    else:
        processing_count = 0
        return 0

def save_processing_count(count):
    with open(COUNT_FILE, "w") as file:
        file.write(str(count))