# What is a queue in programming?
# What is the functionality of multiprocessing.Queue ?
# Why is checking the size of a multiprocessing.Queue sometimes not reliable?
# How to limit the size a multiprocessing.Queue ?
# What happens if you call get(False) on an empty queue? And what does False here stand for?

# The Idea of a Queue
# Pipes and Queues

# Queue implementation in Python
# Queue
# https://www.programiz.com/dsa/queue
# class Queue:
# 
#     def __init__(self):
#         self.queue = []
# 
#     # Add an element
#     def enqueue(self, item):
#         self.queue.append(item)
# 
#     # Remove an element
#     def dequeue(self):
#         if len(self.queue) < 1:
#             return None
#         return self.queue.pop(0)
# 
#     # Display  the queue
#     def display(self):
#         print(self.queue)
# 
#     def size(self):
#         return len(self.queue)
# 
# 
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.enqueue(5)
# 
# q.display()
# 
# q.dequeue()
# 
# print("After removing an element")
# q.display()
 

# Multiprocessing.Queue
#https://www.geeksforgeeks.org/multiprocessing-python-set-2/
# import multiprocessing
#   
# def square_list(mylist, q):
#     # function to square a given list
#     
#     # append squares of mylist to queue
#     for num in mylist:
#         q.put(num * num)
#   
# def print_queue(q):
#     # function to print queue elements
#     print("Queue elements:")
#     while not q.empty():
#         print(q.get())
#     print("Queue is now empty!")
#   
# if __name__ == "__main__":
#     # input list
#     mylist = [1,2,3,4]
#   
#     # creating multiprocessing Queue
#     q = multiprocessing.Queue()
#   
#     # creating new processes
#     p1 = multiprocessing.Process(target=square_list, args=(mylist, q))
#     p2 = multiprocessing.Process(target=print_queue, args=(q,))
#   
#     # running process p1 to square list
#     p1.start()
#     p1.join()
#   
#     # running process p2 to get queue elements
#     p2.start()
#     p2.join()
# 
# 
# functionality of multiprocessing.Queue 
# https://superfastpython.com/multiprocessing-queue-in-python/
# checking the size
# adding maxsize
# prevent blocking


#Task
# works with multiple processes 
# runs them in parallel
# they work with the same queue of objects
# 
# works 2 queues
# 1. task_queue
# 2. done_queue

# task_queue has an object (a list of diffrent balls)
# its loop process will be:
#   bounce once
#   condition to put back to task_queue or put in done_queue
#   take a new ball 
#   every ball has it number of times it can be bounced.
#   if counter reach 0, put in done_queue



import time
from multiprocessing import Process, Queue
from queue import Empty

# leave class Ball as is, don't edit it
class Ball:
    def __init__(self, name, n_bounces):
        self.name = name
        self.n_bounces = n_bounces
    def __str__(self):
        return f'{self.name} ({self.n_bounces})'

# edit the function as described in comments
def bounce(name, delay, task_queue, done_queue):
    global new_ball
    while True:
        time.sleep(delay)
        if done_queue.full():
            print(f"[{name}] done_queue is full. Process will stop.")
            break
        try:
            new_ball = task_queue.get(1, 1)
            new_ball.n_bounces -= 1
            if new_ball.n_bounces == 0:
                done_queue.put(new_ball)
            else:
                task_queue.put(new_ball)
            pass
        except Empty:
            print(f'queue.Empty exception.')
        else:
            pass
            print(f'{name} bounces the {new_ball.name} ({new_ball.n_bounces}).')


# edit the contents of this function in the allowed section
def run_processes(balls, args):
    processes = []
    task_queue = Queue()
    done_queue = Queue(len(balls))

    for ball in balls:
        task_queue.put(ball)
    for name, delay in args:
        new_proc = Process(target=bounce, args=(name, delay, task_queue, done_queue))
        new_proc.start()
        processes.append(new_proc)
    for p in processes:
        p.join()












