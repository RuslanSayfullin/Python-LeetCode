#! /usr/bin/python3
from multiprocessing import Process
import os
import time

# Process — это класс для создания и управления отдельными процессами 
def worker():
    print(f"Worker process with PID: {os.getpid()}")
    time.sleep(2)
    print("Worker process ended")

if __name__ == "__main__":
    print(f"Main process PID: {os.getpid()}")

    p = Process(target=worker)
    p.start()
    print("Worker process started")

    p.join()
    print("Worker process joined")

    print("Main process ended")
