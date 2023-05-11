'''
    Race condition
    Thread Safe
    Dead lock

    A race condition is a situation that can occur in multithreaded or multiprocessing programs
    where the behavior of the program depends on the relative timing or interleaving of the execution
    of concurrent operations. In simpler terms, it refers to a scenario where the output or behavior
    of a program becomes unpredictable because multiple threads or processes are accessing 
    and modifying shared resources concurrently without proper synchronization.

'''


# notice that sometimes it returns 0 without lock but it's not reliable

from threading import Thread, Lock

num = 0 # this variable is a shared resource between the Threads
lock = Lock()

def add():
    global num

    # first method of using lock:
    # lock.acquire()
    # for _ in range(100000):
    #     num += 1
    # lock.release()

    # second method of using lock:
    with lock:
        for _ in range(100000):
            num += 1

def subtract():
    global num
    with lock:
        for _ in range(100000):
            num -= 1
    

t1 = Thread(target=add)
t2 = Thread(target=subtract)

t1.start()
t2.start()

t1.join()
t2.join()

print(num)
print('Done...')