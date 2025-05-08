import os

LOG_FILE = os.path.join(os.path.dirname(__file__), '../logs/keylog.txt')
KEY_FILE = os.path.join(os.path.dirname(__file__), '../fernet.key')

def load_key():
    with open(KEY_FILE, "rb") as f:
        return f.read()
