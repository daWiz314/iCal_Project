MODULES = ['icalendar', 'requests', 'path', 'pytz']

import requests, icalendar, pytz

def check_for_cal():
    '''Checks to see if we have an iCal already, and if we do not then it will go and get it.'''

    default_cal = 'https://ivylearn.ivytech.edu/feeds/calendars/user_qpId1Sh5uICLXEwa517D2Ay1EAnvKsXsNya38lpy.ics'
    cal = requests.get(default_cal)
    # print(cal.content)
    calendar = icalendar.Calendar.from_ical(cal.content)
    # print(calendar)
    
    return calendar


def get_events(cal):
    """Get's all events"""
    all_events = []
    for component in cal.walk():
        if component.name == 'VEVENT':
            all_events.append(component)
    return all_events

def print_events(cal):
    events = get_events(cal)
    for event in events:
        print()
        print("--------------")
        print(event)
        print("--------------")

def attempt_convert_time(cal):
    events = get_events(cal)
    event = events[0]
    print(f"OLD: {event.get('dtstamp').dt}")
    


if __name__ == '__main__':
    for module in MODULES:
        try:
            (f"import {module}")
            print(f"Imported: {module}")
        except ImportError:
            print(f"Could not import {module}!")
    
    print("Imported all modules!")
    cal = check_for_cal()
    # print_events(cal)
    attempt_convert_time(cal)