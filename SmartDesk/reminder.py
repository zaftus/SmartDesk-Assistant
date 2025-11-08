import json
from datetime import datetime
from .config import DATA_DIR
from .utils import load_json, save_json

class Reminder:
    FILE = f"{DATA_DIR}/reminders.json"

    def __init__(self):
        self.reminders = load_json(self.FILE)

    def add_reminder(self, message, time_str):
        self.reminders[message] = time_str
        save_json(self.FILE, self.reminders)
        return f"Reminder added: {message} at {time_str}"

    def list_reminders(self):
        return self.reminders
