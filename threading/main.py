# from scheduleDelay import scheduleWithDelay, add
# import multiprocessing
# from queue import Queue
# import time
# import threading
#
# q= Queue(50)
#
# def do_stuff():
#     while True:
#         params = q.get()
#         func = params[0]
#         delay = params[1]
#         func_to_call = params[2]
#         args = params[3:]
#         func(func_to_call,delay, *args)
#
# t1= threading.Thread(target=do_stuff,args=())
# t1.start()
#
# for i in range(5000):
#     while q.full():
#         time.sleep(5)
#     print("count", i)
#     q.put((scheduleWithDelay,5,add,i,i+1))

# q.join()


## priority Queue
from scheduleDelay import scheduleWithDelay, add
import multiprocessing
from queue import PriorityQueue
import time
import threading

q= PriorityQueue(10)

def do_stuff():
    while True:
        params = q.get()
        func = params[1]
        delay = params[2]
        func_to_call = params[3]
        args = params[4:]
        func(func_to_call,delay, *args)

t1= threading.Thread(target=do_stuff,args=())
t1.start()

for i in range(40):
    while q.full():
        time.sleep(5)
    print("count", i)
    q.put((i%4 + 1, scheduleWithDelay,5,add,i,i+1))


