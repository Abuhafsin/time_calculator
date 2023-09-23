"""Write a function named add_time that takes in two required parameters and one
 optional parameter:
1. a start time in the 12-hour clock format (ending in AM or PM)
2. a duration time that indicates the number of hours and minutes
3. (optional i.e. by using None) a starting day of the week, case-insensitive
The function should add the duration time to the start time and return the result.

Output Example:
add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
"""


def add_time(start_time, duration_time, start_day=None):
    # Check with period of the day AM or PM
    am_pm_mapping = {'AM': 0, 'PM': 12}

    # parse start_time to extract hour_minute and period of the day.
    hour_minute = start_time.split()[0]
    period_of_day = start_time.split()[1]

    # parse duration_time to extract hours and minutes.
    hours = int(duration_time.split(':')[0])
    minutes = int(duration_time.split(':')[1])

    # calculate total minute of the duration.
    total_minutes = hours * 60 + minutes

    # Calculate the start time in 24-hour format.
    start_hour = int(hour_minute.split(':')[0])
    start_minutes = int(hour_minute.split(':')[1])
    start_hour = start_hour + am_pm_mapping[period_of_day]

    # Calculate the end time in 24-hour format.
    end_hour = (start_hour + ((start_minutes + total_minutes) // 60)) % 24
    end_minute = (start_minutes + total_minutes) % 60

    # Calculate number of days later
    day_later = (start_hour + ((start_minutes + total_minutes) // 60)) // 24

    # Determine AM or PM for the end time
    if end_hour == 0:
        end_period_of_day = 'AM'
        end_hour = 12
    elif end_hour < 12:
        end_period_of_day = 'AM'
        end_hour = end_hour
    elif end_hour == 12:
        end_period_of_day = 'PM'
        end_hour = 12
    else:
        end_period_of_day = 'PM'
        end_hour -= 12

    # Format the result time in 12 hours clock
    result_time = f"{end_hour:02d}:{end_minute:02d} {end_period_of_day}"

    # Format the day of the week if starting_day is provided.
    if start_day:
        start_day = start_day.capitalize()
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        start_day_index = days.index(start_day)
        end_day_index = (start_day_index + day_later) % 7
        result_day = days[end_day_index]

    # Include the day of the week in the output.
    if start_day:
        result_time += f', {result_day}'

    # Format the result string with days later.
    if day_later == 1:
        result_time += f' (next day)'
    elif day_later > 1:
        result_time += f' ({day_later} days later)'

    return result_time


if __name__ == '__main__':
    print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

    print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

    print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

    print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

    print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

    print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)

