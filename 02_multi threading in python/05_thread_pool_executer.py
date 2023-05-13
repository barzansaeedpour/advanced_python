'''
In Python, you can use the concurrent.futures module to implement a thread pool executor.
The ThreadPoolExecutor class provides an easy-to-use interface for managing a pool of worker threads.
Here's an example of how you can use it:
'''

from time import sleep
from concurrent.futures import ThreadPoolExecutor

def show(name):
    print(f'{name} started.')
    sleep(3)
    print(f'{name} finished.')

# the best way of using ThreadPoolExecutor is to use as a context manager:

with ThreadPoolExecutor() as executer:
    names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight']
    executer.map(show, names)

# if we want to execute the threads two by two:

# with ThreadPoolExecutor(max_workers=2) as executer:
#     names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight']
#     executer.map(show, names)

print('Done ...')


