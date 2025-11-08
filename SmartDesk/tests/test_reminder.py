from smartdesk.reminder import Reminder

def test_add_reminder():
    rem = Reminder()
    rem.add_reminder("Test", "10:00")
    assert "Test" in rem.list_reminders()
