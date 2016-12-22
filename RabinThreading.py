

from time import time
import threading
import sys


numThreads = 4
numTests = 1
class ThreadWithReturnValue(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        threading.Thread.__init__(self, group, target, name, args, kwargs, daemon=daemon)

        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self):
        threading.Thread.join(self)
        return self._return


def string2numeric_hash(text):
    import hashlib
    return int(hashlib.md5(text).hexdigest()[:8], 16)

def RabinCDC(LBAlist):
    P = 53424
    a = 10
    rolling_hash = 0
    n = len(LBAlist)
    breakindices = []
    for i in range(a,n-1):
        rolling_hash += sum(LBAlist[i-a:i])
        secondhash = string2numeric_hash(str(rolling_hash).encode('utf-8'))
        if secondhash%9 == 0:
            breakindices.append(i)
            rolling_hash = 0
    return breakindices




def threadingTest(src):
    print("Testing Source File: " + str(src))
    target = open(src, 'r')
    global LBAlist
    LBAlist = target.readlines()
    LBAlist = [int(x) for x in LBAlist]

    global numProcs
    avgTime = [0 for x in range(numProcs )]

    for i in range(numTests):
        start = time()
        serialResult = serialCode(LBAlist)
        t = time() - start
        #print(t)
        print("Time for 1 Processors: {0}".format(t))
        avgTime[0] = avgTime[0] + t/numTests
    print(avgTime)
    #print(serialResult)
    #MultiProcessor Run
    for i in range(2, numProcs + 1):
        for test in range(numTests):
            start = time()
            chunkSize = int(len(LBAlist)/numProcs)
            jobs = []
            listq = []
            for p in range(0,i):
                if p != i-1:
                    thr = ThreadWithReturnValue(target = RabinCDC, args = [LBAlist[chunkSize*p:chunkSize*(p+1)]])
                else:
                    thr = ThreadWithReturnValue(target = RabinCDC, args = [LBAlist[chunkSize*p:]])
                thr.start()
                jobs.append(thr)
            #Process Synchronization
            resultL = []
            for thr in jobs:
                print("Try")
                #print("We got here")
                resultL += thr.join()
                #print("Hi")

            #print(resultL)
            #print(newPool)
            #print(len(newPool))
            t2 = time() - start
            #print(t2)
            avgTime[i - 1] += t2/numTests
            print("Time for {0} Threads: {1}".format(i, t2))
        print(avgTime)
    resultFile = open('threadingTimes.txt', 'a+')
    resultFile.write(src + '\n')
    for testTime in avgTime:
        resultFile.write(str(testTime) + " ")
    resultFile.write('\n')