import threading
import time

globalCount = 0

def printMultipleOf3(lock):
    # global globalCount
    currCount = 0
    while(globalCount < 100):

        lastGlobalDigit = globalCount % 10
        lastCurrDigit = currCount % 10
        
        if globalCount == 0 or (lastGlobalDigit == lastCurrDigit and lastGlobalDigit in [1 ,2, 6, 7]):
            lock.acquire()
            currCount += 3
            globalCount = currCount
            print(globalCount)
            lock.release()
        elif lastGlobalDigit in [0, 5]:
            lock.acquire()
            currCount += 3
            globalCount = currCount
            print(globalCount)
            lock.release()
        time.sleep(1)

def printMultipleOf5(lock):
    # print("printMultipleOf5")
    # global globalCount
    currCount = 0
    while(globalCount < 100):
        # print(globalCount)
        lastGlobalDigit = globalCount % 10
        lastCurrDigit = currCount % 10

        if lastGlobalDigit != lastCurrDigit and lastGlobalDigit in [0 ,3, 4, 5, 8, 9]:
            lock.acquire()
            currCount += 5
            globalCount = currCount
            print(globalCount)
            lock.release()
        time.sleep(1)


lock = threading.Lock()
printMultipleOf3Thread = threading.Thread(target=printMultipleOf3, args=(lock,))
printMultipleOf5Thread = threading.Thread(target=printMultipleOf5, args=(lock,))

printMultipleOf5Thread.start()
printMultipleOf3Thread.start()

printMultipleOf3Thread.join()
printMultipleOf5Thread.join()




