# What is a thread in programming?
# What is multithreading (in programming)?
# Which module must be used to work with threads in Python?
# How to create a thread? What arguments are required?
# How to start a thread?

# An Intro to Threading in Python
# Python - Multithreaded Programming
# Python - Date and Time


# when task run in order, it is asyncronus
# threading makes the tasks run almost syncronusly

## https://www.youtube.com/watch?v=IEEhzQoKtQU
#
#import concurrent.futures
#import time
#import threading
#
#start = time.perf_counter()
#
#def do_something(seconds):
#    print(f'Sleeping {seconds} second(s)...')
#    time.sleep(seconds)
#    return f'Done sleeping...{seconds}'
#
#########using concurrent futures module#######
#with concurrent.futures.ThreadPoolExecutor() as executor:
#    secs = [5, 4, 3, 2, 1]
#    #######using as_completed######
#    results = [executor.submit(do_something, sec) for sec in secs]
#    for f in concurrent.futures.as_completed(results):
#        print(f.result())
#
#    #######using map#######
#    #results = executor.map(do_something, secs)
#    #for result in results:
#    #    print(result)
#
#######using threading moudule#######
## threads = [] 
## for _ in range(10):
##     t = threading.Thread(target=do_something, args=[1.5])
##     t.start()
##     threads.append(t)
## for thread in threads:
##     thread.join()
#
#finish = time.perf_counter()
#
#print(f'Finished in {round(finish-start, 2)} second(s)')



import threading
import time

def task_thread(name, path, delay):
    with open(path, 'r') as file:
        for line in file:
            print(f'[{name}]: {line[:-1]}') #line[:-1] from start to last number in a line, and cut out /n
            time.sleep(delay)

def start_threads(jobs):
    for task in jobs:
        t = threading.Thread(target=task_thread, args=(task['name'], task['path'], task['delay']))
        t.start()



