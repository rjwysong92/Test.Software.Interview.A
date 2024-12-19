import numpy as np
import pint


#create a unit registry
ureg = pint.UnitRegistry()

# Define the time in seconds, minutes, and hours
time_seconds = 60 * ureg.second
time_minutes = 1 * ureg.minute
time_hours = 1 * ureg.hour

# Convert the time in hours to minutes and seconds
time_in_minutes = time_hours.to(ureg.minute)
time_in_seconds = time_minutes.to(ureg.second)

def total_time_in_seconds(time_in_minutes, time_in_seconds):
    """
    Calculate the total time in seconds.

    Args:
        time_in_minutes (int): The time in minutes.
        time_in_seconds (int): The time in seconds.

    Returns:
        int: The total time in seconds.
    """
    print(f"total_time_in_seconds: {total_time_in_seconds}")