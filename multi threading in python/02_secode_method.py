from time import sleep, perf_counter
from threading import Thread

print('*** normal execution ***')

start = perf_counter()

def show(name, delay):
    print(f'{name} started.')
    sleep(delay)
    print(f'{name} finished.')

show('One', 3)
show('Two', 3)
end = perf_counter()
print(end - start)

######################## multi-threading #########################

print('*** using multi-threading ***')

start = perf_counter()

class ShowThread(Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        show(self.name, self.delay)

t1 = ShowThread('One', 3)
t2 = ShowThread('Two', 3)

t1.start()
t2.start()

t1.join()
t2.join()

end = perf_counter()

print('using multi-threading: ', end - start)


