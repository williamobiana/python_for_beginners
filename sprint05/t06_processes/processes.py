# What is a process in programming?
# What is multiprocessing (in programming)?
# Which module must be used to work with processes in Python?
# How to create a process? What arguments are required?
# How to start a process?
# What are the differences in working with threads and processes?

# Multiprocessing Vs. Threading In Python: What You Need To Know.
# multiprocessing — Process-based parallelism

# https://www.geeksforgeeks.org/multiprocessing-python-set-1/
import multiprocessing
  
def print_cube(num):
    #function to print cube of given num
    print(f"Cube: {num * num * num}")
  
def print_square(num):
    # function to print square of given num
    print(f"Square: {num * num}")

# Execute  
if __name__ == "__main__":
    # create processes
    p1 = multiprocessing.Process(target=print_square, args=(10, ))
    p2 = multiprocessing.Process(target=print_cube, args=(10, ))
  
    # start process 1
    p1.start()
    # start process 2
    p2.start()
  
    # wait until process 1 is finished
    p1.join()
    # wait until process 2 is finished
    p2.join()
  
    # both processes finished
    print("Done!")


# Print the ID of the processes running the target functions
import multiprocessing
import os
  
def worker1():
    # printing process id
    print(f"ID of process running worker1: {os.getpid()}")
  
def worker2():
    # printing process id
    print(f"ID of process running worker2: {os.getpid()}")

# Execute 
if __name__ == "__main__":
    # printing main program process id
    print(f"ID of main process: {os.getpid()}")
  
    # creating processes
    p1 = multiprocessing.Process(target=worker1)
    p2 = multiprocessing.Process(target=worker2)
  
    # starting processes
    p1.start()
    p2.start()
  
    # process IDs
    print(f"ID of process p1: {p1.pid}")
    print(f"ID of process p2: {p2.pid}")
  
    # wait until processes are finished
    p1.join()
    p2.join()
  
    # both processes finished
    print("Both processes finished execution!")
  
    # check if processes are alive
    print(f"Process p1 is alive: {p1.is_alive()}")
    print(f"Process p2 is alive: {p2.is_alive()}")



# Communication between processes
import multiprocessing
  
# empty list with global scope
result = []
  
def square_list(mylist):
    # function to square a given list
    global result
    # append squares of mylist to global list result
    for num in mylist:
        result.append(num * num)
    # print global list result
    print(f"Result(in process p1): {result}")

# Execute   
if __name__ == "__main__":
    # input list
    mylist = [1,2,3,4]
  
    # creating process
    p1 = multiprocessing.Process(target=square_list, args=(mylist,))
    # starting process
    p1.start()
    # wait until process is finished
    p1.join()
  
    # print global result list
    print(f"Result(in main program): {result}")








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

