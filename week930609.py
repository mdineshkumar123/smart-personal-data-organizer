import time

def set_reminder(msg, seconds):
    print("Waiting...")
    time.sleep(seconds)
    print("🔔 Reminder:", msg)

if __name__ == "__main__":
    set_reminder("Study Python", 5)