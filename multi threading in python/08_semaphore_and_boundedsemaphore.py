'''
    In Python, a semaphore is a synchronization primitive provided by the threading module. 
    It is used to control access to a shared resource or a limited number of resources. 
    Semaphores allow multiple threads to access a resource simultaneously up to a specified limit.
'''

'''
    In this example, a semaphore with a limit of 3 resources is created using threading.Semaphore(3). 
    The worker_func represents the work that needs to be performed by the worker threads. 
    Each worker thread first acquires a resource from the semaphore using semaphore.acquire(). 
    If a resource is available (counter > 0), it proceeds with its work. Otherwise, 
    if all resources are currently in use (counter = 0), the thread will be blocked until a 
    resource becomes available.

    After completing its work, the thread releases the resource back to the semaphore using 
    semaphore.release(). This allows another thread to acquire the resource and continue its work.

    In this example, even though there are more than 3 worker threads, 
    only 3 threads can acquire resources from the semaphore simultaneously. 
    The other threads will be blocked until resources become available.

    Semaphores are useful in scenarios where you want to limit the number of concurrent 
    accesses to a particular resource or when you want to control the number of threads 
    that can execute a specific section of code simultaneously.
'''



import threading

# Create a semaphore with a limit of 3 resources
semaphore = threading.Semaphore(3)

'''
    In Python, BoundedSemaphore is a variant of the Semaphore class provided by the threading module. 
    It behaves similarly to a regular semaphore but with an added upper bound on the number of available 
    resources. This upper bound restricts the number of release() calls that can be made on the 
    BoundedSemaphore.
'''
semaphore = threading.BoundedSemaphore(3)

def worker_func(worker_id):
    # Acquire a resource from the semaphore
    semaphore.acquire()
    print(f"Worker {worker_id} acquired a resource")

    # Perform some work
    print(f"Worker {worker_id} is working...")

    # Release the resource back to the semaphore
    semaphore.release()
    print(f"Worker {worker_id} released the resource")

# Create multiple worker threads
num_workers = 5
worker_threads = []
for i in range(num_workers):
    worker_thread = threading.Thread(target=worker_func, args=(i,))
    worker_threads.append(worker_thread)
    worker_thread.start()

# Wait for the worker threads to complete
for worker_thread in worker_threads:
    worker_thread.join()
