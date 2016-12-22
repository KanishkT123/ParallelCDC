from multiprocessing import Pool
from time import time
def sum_nums(args):
    low = int(args[0])
    high = int(args[1])
    return sum(range(low,high+1))

def testCode(n, procs):
    results = []
    sizeSegment = n/procs

    if procs == 1:
        start = time()
        print(sum_nums([0, n]))
        t = time() - start
        print("Serial Runtime:" + str(t))
        return [procs, t]


    # Multiprocessing version 
    # Create size segments list
    start2 = time()
    jobs = []
    for i in range(0, procs):
        jobs.append((i*sizeSegment+1, (i+1)*sizeSegment))

    pool = Pool(procs).map(sum_nums, jobs)
    print(pool)
    result = sum(pool)
    print(result)
    t = time() - start2
    print("Parallel Runtime ({0} Workers):".format(procs) + str(time() - start2))
    return [procs, t]

if __name__ == "__main__":
    results = []
    n = 1
    print(hash(int))
    print(hash('420'))
    for i in range(1, n + 1):
        results.append(testCode(10, i))
    print(results)

