'''
This is a python implementation of Fixed Window Chunking.
Author: Kanishk Tantia, Jason Ma
Date:  December 3rd, 2016
'''
import sys
from multiprocessing import Pool
from time import time

def parallel(src, procs):
        '''
    Input: data buffer src
    '''
    target = open(src, 'r')
    LBAlist = len(target.readlines())

    n = 8

    breakindices = []
    jobs = []
    sizeSegment = LBAlist/procs
    for i in range(0, procs):
        jobs.append((i*sizeSegment+1, (i+1)*sizeSegment))


    for i in range(1,LBAlist):
        if i%n == 0:
            breakindices.append(i)
        elif i == LBAlist:
            breakindices.append(i)

    outputfile = open("FixedOutput", 'w')
    for i in breakindices:
        outputfile.write("%s\n" % i)

    outputfile.close()

def serial(src):
   
    '''
    Input: data buffer src
    '''
    target = open(src, 'r')
    LBAlist = len(target.readlines())

    n = 8

    breakindices = []

    for i in range(1,LBAlist):
    	if i%n == 0:
    		breakindices.append(i)
    	elif i == LBAlist:
    		breakindices.append(i)

    outputfile = open("FixedOutput", 'w')
    for i in breakindices:
        outputfile.write("%s\n" % i)

    outputfile.close()

def main(src):
    start = time()
    parallel(src, 5)
    t = time() - start

    start2 = time()
    serial(src)
    t2 = time() - start2


if __name__ == '__main__':
    if len(sys.argv) == 2:
        src = sys.argv[1] # data buffer
        main(src)
    else:
        print "Usage: fixedc.py <databuffer>"