from time import sleep, perf_counter
from threading import Thread, current_thread, enumerate


# enumerate returns a list of all Thread objects alive.

start = perf_counter()

def show(name):
    print(f'{name} started.')
    print(current_thread().name, ' is running.')
    sleep(3)
    print(f'{name} finished.')


t1 = Thread(target=show, args=('One',), name= 'First')
t2 = Thread(target=show, args=('Two',), name= 'Second')
t1.start()
t2.start()

print('current threads alive: ', enumerate())

t1.join() # wait until thread t1 is finished
t2.join() # wait until thread t2 is finished

end = perf_counter()

print(end - start)


