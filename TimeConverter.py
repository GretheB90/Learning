from datetime import datetime #I want to use the clock!
import pytz #knows about all the world’s time zones

def get_time_in_copenhagen():
    #Gets the current time in Copenhagen's timezone:
    copenhagen_timezone = pytz.timezone("Europe/Copenhagen")
    return datetime.now(copenhagen_timezone)

def convert_time(copenhagen_time, target_timezone_str):
    #Converts Copenhagen time to another timezone:
    target_timezone = pytz.timezone(target_timezone_str)
    return copenhagen_time.astimezone(target_timezone)

#Get current time in Copenhagen:
copenhagen_time = get_time_in_copenhagen()

#Convert to other timezones:
japan_time = convert_time(copenhagen_time, "Asia/Tokyo")
new_york_time = convert_time(copenhagen_time, "America/New_York")
los_angeles_time = convert_time(copenhagen_time, "America/Los_Angeles")

#Format using AM/PM: %I = hour (12-hour), %p = AM/PM
time_format = "%Y-%m-%d %I:%M:%S %p"

#Print all times in AM/PM format
print("Current time in Copenhagen:  ", copenhagen_time.strftime(time_format))
print("Current time in Japan:       ", japan_time.strftime(time_format))
print("Current time in New York:    ", new_york_time.strftime(time_format))
print("Current time in Los Angeles: ", los_angeles_time.strftime(time_format))

#Symbol:  Meaning:                    Example:
# %Y    - 4-digit year - example:     - 2025
# %m    - 2-digit month (01 to 12)    - 08
# %d    - 2-digit day (01 to 31)      - 18
# %H    - 2-digit hour (00 to 23)     - 15
# %M    - 2-digit minute (00 to 59)   - 30
# %S    - 2-digit second (00 to 59)   - 00
# %p    - AM or PM                    - PM

#copenhagen_time.strftime("%Y-%m-%d %H:%M:%S")
#Will turn into this: 2025-08-18 15:30:00
