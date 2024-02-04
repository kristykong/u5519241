def speeding_ticket(speed, is_birthday):
    # Adjust speed limits if it's the driver's birthday
    speed_adjustment = 5 if is_birthday else 0
    
    # Define speed limits
    no_ticket_limit = 60 + speed_adjustment
    small_ticket_limit = 80 + speed_adjustment
    
    # Determine ticket type based on speed
    if speed <= no_ticket_limit:
        return "No Ticket"
    elif speed <= small_ticket_limit:
        return "Small Ticket"
    else:
        return "Big Ticket"


print(speeding_ticket(60, False)) 

