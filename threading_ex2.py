import threading
import time

def count_down(n):
    for i in range(n,-1,-1):
        print("Running thread1....")
        print(i)
        time.sleep(1)


def count_up(n):
    for i in range(n+1):
        print("Running thread2...")
        print(i)
        time.sleep(1)

thread1 = threading.Thread(target=count_down,args=(10,))
thread2 = threading.Thread(target=count_up,args=(5,))
thread1.start()
thread2.start()
