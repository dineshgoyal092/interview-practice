import threading
import time

def add(args):
    x = args[0]
    y = args[1]
    print(x+y)

def execute_delay(func, args, delay):
    # print("hello")
    time.sleep(delay)
    func(args)
    
def scheduleWithDelay(func, delay, *args):
    # def inner_fn():
    #     return func(*args)
    # t = threading.Thread(target=execute_delay, args=(func,args, delay))
    # inner_fn()
    print(args)
    t = threading.Thread(target=execute_delay, args=(func,args, delay))
    t.start()
    threading.Timer(1, func, args).start()


if __name__ == '__main__':
    scheduleWithDelay(add,5, 2, 3)







# from time import sleep
# import threading
#
# class Scheduler:
#     def __init__(self):
#         self.fns = [] # tuple of (fn, time)
#         t = threading.Thread(target=self.poll)
#         t.start()
#
#     def poll(self):
#         while True:
#             now = time() * 1000
#             for fn, due in self.fns:
#                 if now > due:
#                     fn()
#             self.fns = [(fn, due) for (fn, due) in self.fns if due > now]
#             sleep(0.01)
#
#     def delay(self, f, n):
#         self.fns.append((f, time() * 1000 + n))
