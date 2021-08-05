from models.event import *
import datetime

event1 = Event("10/08/21", "Wedding", 200, "Garden", "Tom and Sally marriage")
event2 = Event("11/08/21", "Birthday Party", 30, "Piano Room", "Grandad's 90th")
events = [event1, event2]

def add_new_event(event):
    events.append(event)