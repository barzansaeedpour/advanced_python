from time import sleep, perf_counter
from threading import Thread
import sys

# When daemon is False, the program does not exit until the thread is finished.
# But, when daemon is True, the program exits whether the thread is finished or not.
# In the example below, daemon is True. Therefore, the program exits on sys.exit() command even though the 
# threads are not finished yet.  


start = perf_counter()

def show(name):
    print(f'{name} started.')
    sleep(3)
    print(f'{name} finished.')

# daemon is False by default
t1 = Thread(target=show, args=('One',), daemon= True)
t2 = Thread(target=show, args=('Two',), daemon= True)

# another way of setting daemon value is to use the setter:
# t1.setDaemon(True)
# t2.setDaemon(True)

t1.start()
t2.start()

print(t1.isDaemon())
print(t2.isDaemon())

# When we use join, deamon value does not matter.

# t1.join() # wait until thread t1 is finished
# t2.join() # wait until thread t2 is finished

end = perf_counter()

print('using multi-threading: ', end - start)
sys.exit()


