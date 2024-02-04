from datetime import datetime

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
date_passed("26th March", "25th March")  
date_passed("26th March", "26th March") 
date_passed("26th March", "27th March") 
