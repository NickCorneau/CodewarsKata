def evaporator(content, evap_per_day, threshold):
    # initialize date
    day = 0
    
    # set evap to its compliment 
    # in order to allow multiplication
    evap = (100 - evap_per_day) * 0.01
    content = 100.
    
    while (content >= threshold):
        content *= evap
        day += 1

    return day