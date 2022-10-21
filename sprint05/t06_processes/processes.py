# What is a process in programming?
# What is multiprocessing (in programming)?
# Which module must be used to work with processes in Python?
# How to create a process? What arguments are required?
# How to start a process?
# What are the differences in working with threads and processes?

# Multiprocessing Vs. Threading In Python: What You Need To Know.
# multiprocessing — Process-based parallelism

# https://www.youtube.com/watch?v=fKl2JW_qrso



from multiprocessing import Process
import datetime, time


def task_process(name, year, delay):
    date_now = datetime.datetime.now().year
    print(f"{name}, {date_now - year} years old")
    time.sleep(delay)

def start_processes(jobs):
    for task in jobs:
        p = Process(target=task_process, args=(task['name'], task['year'], task['delay']))
        p.start()

