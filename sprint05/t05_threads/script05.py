from threads import task_thread, start_threads


if __name__ == '__main__':

    jobs = [
        {'name': 'Thread 1', 'path': 'file1.txt', 'delay': 3},
        {'name': 'Thread 2', 'path': 'file2.txt', 'delay': 1},
        {'name': 'Thread 3', 'path': 'file1.txt', 'delay': 5},
    ]

    start_threads(jobs)