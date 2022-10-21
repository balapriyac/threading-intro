import threading
import time

def some_func():
    print("Running some_func...")
    time.sleep(2)
    print("Finished running some_func.")

thread1 = threading.Thread(target=some_func)
thread1.start()
thread1.join()
print(threading.activeCount())
