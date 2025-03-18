import time
from datetime import datetime

def date_to_timestamp(date: str) -> int:
    try:
        try:
            date_time = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            date_time = datetime.strptime(date, '%Y-%m-%d')
            date_time = date_time.replace(hour=0, minute=0, second=0)

        time_tuple = date_time.timetuple()
        timestamp = time.mktime(time_tuple)
        return int(timestamp)
    except Exception as error:
        print(f"Error: {error}")
