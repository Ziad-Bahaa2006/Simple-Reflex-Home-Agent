def lighting_agent(motion,time_of_day,light_level):
        # Rule 1: Night + Motion → ON
    if motion == "yes" and time_of_day == "night" and light_level == "low":
        return "Light ON (High Brightness)"
    
    # Rule 2: Night + Motion (normal)
    elif motion == "yes" and time_of_day == "night":
        return "Light ON"
    
    # Rule 3: Night + No Motion → OFF
    elif motion == "no" and time_of_day == "night":
        return "Light OFF"
    
    # Rule 4: Day + Motion → OFF (save energy)
    elif motion == "yes" and time_of_day == "day":
        return "Light OFF"
    
    # Rule 5: Day + No Motion → OFF
    elif motion == "no" and time_of_day == "day":
        return "Light OFF"
    
    # Default
    else:
        return "No Action"