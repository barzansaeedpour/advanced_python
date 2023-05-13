'''
    what is dead lock:
        A deadlock is a situation that can occur in multithreaded or multiprocessing programs
        where two or more threads or processes are unable to proceed because each is waiting 
        for the other to release a resource or take some action. As a result, the program 
        becomes stuck and cannot make progress.

        In Python, deadlocks can occur when multiple threads or processes acquire locks or resources 
        in a way that creates a circular dependency. This situation can arise when the threads or 
        processes acquire multiple locks or resources and the order of acquisition is not consistent 
        across all threads or processes.
    
    How to solve a dead lock:
        In Python, RLock stands for "reentrant lock," which is a variation of the standard Lock object
        provided by the threading module. The RLock class allows multiple consecutive acquisitions 
        of the lock by the same thread without causing a deadlock. It provides a reentrant mechanism, 
        meaning a thread can acquire the lock multiple times and must release it the same number of 
        times to fully unlock it.
'''

import threading

# Two resources (locks)
resource1_lock = threading.Lock()
resource2_lock = threading.Lock()

# to fix the dead lock issue in this example, we need to use Rlock:

# resource1_lock = threading.RLock()
# resource2_lock = threading.RLock()



def thread1_func():
    with resource1_lock:
        print("Thread 1 acquired resource 1")
        with resource2_lock:
            print("Thread 1 acquired resource 2")

def thread2_func():
    with resource2_lock:
        print("Thread 2 acquired resource 2")
        with resource1_lock:
            print("Thread 2 acquired resource 1")

# Create two threads
thread1 = threading.Thread(target=thread1_func)
thread2 = threading.Thread(target=thread2_func)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to complete
thread1.join()
thread2.join()

'''
    In this example, there are two threads that acquire two resources (resource1_lock and resource2_lock). 
    thread1 first acquires resource1_lock and then attempts to acquire resource2_lock, while thread2 first 
    acquires resource2_lock and then attempts to acquire resource1_lock. If the timing is unfortunate, 
    it can lead to a deadlock situation.
    If thread1 acquires resource1_lock and thread2 acquires resource2_lock simultaneously, 
    both threads will be blocked when they try to acquire the second resource, resulting in a deadlock. 
    Each thread is waiting for the other to release the resource it needs, preventing both threads 
    from making progress.
'''