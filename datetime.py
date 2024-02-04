"""
Date Scheduler Function

Objective:
Write a function named 'date_passed' to determine the relationship between two dates.

Function Parameters:
1. todays_date (string): The current date in the format 'day Month'.
2. scheduled_date (string): The scheduled date to compare, in the same format.

Instructions:
- The function should compare todays_date and scheduled_date and print whether the scheduled date has passed, is yet to pass, or is today.
- Assume the dates are in the same year.
- The dates are in a format like '26th March'. Consider how to convert these for comparison.
- https://www.w3schools.com/python/python_datetime.asp

Example Test Cases:
1. date_passed('26th March', '25th March') should indicate that the scheduled date has passed.
2. date_passed('26th March', '26th March') should indicate that the scheduled date is today.
3. date_passed('26th March', '27th March') should indicate that the scheduled date is yet to pass.
"""


def date_passed(todays_date, scheduled_date):
    # Remove the ordinal suffix
    todays_date = ''.join([i for i in todays_date if not i.isdigit()]) + ' ' + ''.join([i for i in todays_date if i.isdigit()])
    scheduled_date = ''.join([i for i in scheduled_date if not i.isdigit()]) + ' ' + ''.join([i for i in scheduled_date if i.isdigit()])
    
    date_format = '%d %B'
    
    # Assume the current year for both dates to compare
    current_year = datetime.now().year
    todays_date_str = f"{current_year} {todays_date}"
    scheduled_date_str = f"{current_year} {scheduled_date}"
    
    # Convert strings to datetime objects
    todays_datetime = datetime.strptime(todays_date_str, f"%Y {date_format}")
    scheduled_datetime = datetime.strptime(scheduled_date_str, f"%Y {date_format}")
    
    # Compare the two datetime objects
    if todays_datetime > scheduled_datetime:
        print("Scheduled date has passed")
    elif todays_datetime < scheduled_datetime:
        print("Scheduled date is yet to pass")
    else:
        print("Scheduled date is today")


# Test cases
date_passed("26th March", "25th March")  # Expected: Scheduled date has passed
date_passed("26th March", "26th March")  # Expected: Scheduled date is today
date_passed("26th March", "27th March")  # Expected: Scheduled date is yet to pass

