'''
    To create a timer using the threading module in Python, you can utilize the Timer class. 
    The Timer class allows you to execute a function after a specified delay. 
    Here's an example:
'''

import threading

def timer_callback():
    print("Timer complete!")

# Create a timer that will execute the callback after 5 seconds
timer = threading.Timer(5, timer_callback)
timer.start()

# Do other tasks while the timer is running
print("Doing other tasks...")

# Wait for the timer to complete
timer.join()

print("Timer finished.")

'''
    In this example, a timer is created using threading.Timer(5, timer_callback), 
    where 5 represents the delay in seconds and timer_callback is the function that will be 
    executed when the timer completes. The start() method starts the timer, and the main 
    thread continues to execute other tasks while the timer is running.

    The timer.join() call is used to block the main thread until the timer completes. 
    This is optional but can be useful if you want to wait for the timer to finish before 
    proceeding with other actions.

    When the timer completes, the timer_callback() function is executed, and "Timer complete!" i
    s printed. Finally, "Timer finished." is printed to indicate that the timer has finished execution.
'''