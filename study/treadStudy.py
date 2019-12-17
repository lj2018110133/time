import threading
import time

lock = threading.Lock()


def action(max_a):
    with lock:
        for i in range(max_a):
            print(threading.current_thread().getName() + " " + str(i))


def action_c(max_c):
    if lock.acquire(1):
        for i in range(max_c):
            print(threading.current_thread().getName() + " " + str(i))
            time.sleep(1)
        lock.release()


for i in range(30):
    # print(threading.current_thread().getName() + " " + str(i))
    if i == 20:
        t1 = threading.Thread(target=action_c, args=(30,))
        t1.start()
        t2 = threading.Thread(target=action_c, args=(30,))
        t2.start()
time.sleep(35)
print("主线程执行结束")
