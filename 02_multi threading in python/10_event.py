'''
    In Python's threading module, an event object is a synchronization primitive that allows threads 
    to communicate with each other. It provides a simple mechanism for threads to wait for a specific 
    event to occur.

    The Event class in the threading module represents an event object. 
    It has two main methods: wait() and set().

    wait(): This method blocks the thread until the event is set. If the event is already set, 
            the thread continues execution immediately.

    set(): This method sets the event, allowing any waiting threads to proceed. 
           If multiple threads are waiting for the event, only one of them will proceed, 
           and the rest will continue to wait until the event is set again.

    Here's an example that demonstrates the usage of an event object:
'''

import threading
import time

def wait_for_event(event):
    print("Thread waiting for event.")
    event.wait()
    print("Thread received event.")

# Create an event object
event = threading.Event()

# Create and start a thread that waits for the event
thread = threading.Thread(target=wait_for_event, args=(event,))
thread.start()

# Perform some tasks
print("Main thread performing some tasks...")

# Wait for a few seconds
time.sleep(2)

# Set the event to signal the waiting thread
event.set()

# Wait for the thread to complete
thread.join()

print("Main thread finished.")


'''
    In this example, the wait_for_event function represents a thread that waits for the 
    event to be set. It calls event.wait() to block until the event is set. 
    The main thread sets the event after a delay of 2 seconds using event.set().

    When the event is set, the waiting thread proceeds and prints "Thread received event." 
    Finally, the main thread waits for the waiting thread to finish using thread.join(), 
    and "Main thread finished." is printed.

    Note that if the event is already set when event.wait() is called, 
    the thread calling wait() will continue without blocking. 
    If you want to reset the event after it is set, you can use the clear() method on 
    the event object.
'''