from .automation import Automation
from .reminder import Reminder

class SkillManager:
    def __init__(self):
        self.skills = {
            "organize": self.organize,
            "reminder": self.reminder
        }
        self.automation = Automation()
        self.reminder_system = Reminder()

    def run_skill(self, command, args):
        for key in self.skills:
            if key in command.lower():
                return self.skills[key](args)
        return "No matching skill found."

    def organize(self, args):
        path = args.get("path", ".")
        self.automation.organize_folder(path)
        return f"Organized folder: {path}"

    def reminder(self, args):
        message = args.get("message", "No message")
        time_str = args.get("time", "No time")
        return self.reminder_system.add_reminder(message, time_str)
