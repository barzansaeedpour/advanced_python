from time import sleep, perf_counter
from threading import Thread

print('*** normal execution ***')

start = perf_counter()

def show(name):
    print(f'{name} started.')
    sleep(3)
    print(f'{name} finished.')

show('One')
show('Two')
end = perf_counter()
print(end - start)

######################## multi-threading #########################

print('*** using multi-threading ***')
start = perf_counter()
t1 = Thread(target=show, args=('One',))
t2 = Thread(target=show, args=('Two',))
t1.start()
t2.start()

t1.join() # wait until thread t1 is finished
t2.join() # wait until thread t2 is finished

end = perf_counter()

print('using multi-threading: ', end - start)


