'''
This is a python implementation of FastCDC.
Author: Kanishk Tantia, Jonathan Cruz
Date:  June 7th, 2016

Pseudocode:
Input: data buffer, src; buffer length, n
Output: chunking breakpoint i
Macro Defined: Mask <-- 0x7
Macro Defined: MinSize <-- 2KB; MaxSize <-- 64KB;
    fp <-- 0; i <-- MinSize; NormalSize <-- 8KB;
if n <= MinSize then
    return n;
if n >= MaxSize then
    n <-- MaxSize;
else if n <= NormalSize then
    n <-- NormalSize;
for ; i < n; i++; do
    fp = (fp << 1) + Gear[src[i]];
    if ! (fp & Mask) then
        return i; // if the masked bits are all '0'
return i;
'''
import sys

MIN_SIZE = 8
MAX_SIZE = 20
I = 0
HASH = 0
GEAR = []
import random

def gear_gen():
    global GEAR
    x = []
    for i in range(0, 256):
        y = random.getrandbits(64)
        x.append(y)
    target = open("randoms", 'w')
    GEAR = x
    for item in x:
        target.write("%s\n" % item)


def blockbreak(LBA):
    '''Takes a single block as string input. Converts it to a 40 bit binary number.
    Uses GEAR to do a lookup on each of the 8 bits and adds that to a running total.
    The running total is then checked to see if it ends with "000".
    '''
    global HASH
    binLBA = '{0:040b}'.format(int(LBA)) #Converts integer to 40 bit binary
    n = 8
    splitLBA = [binLBA[i:i+n] for i in range(0, len(binLBA), n)] #Splits binary every 8 bits and adds to list
    for binary in splitLBA:
        HASH <<= 1
        HASH += int(GEAR[int(binary, 2)]) #Converts each 8 bit binary into integer and adds it to HASH

def parallelcdc(a0, a1):
    
def main(src):
    '''
    Input: data buffer src
    '''
    global I
    global GEAR
    global HASH

    try:
        target = open("randoms", 'r')
        GEAR = target.readlines()
        target.close()
    except:
        gear_gen()

    target = open(src, 'r')

    LBAlist = target.readlines()

    breakindices = []

    for num in range(len(LBAlist)):
        blockbreak(LBAlist[num])
        I += 1
        if I <= MIN_SIZE:
            if num == len(LBAlist)-1:
                breakindices.append(num)
                break
            continue
        elif I >= MAX_SIZE:
            breakindices.append(num)
            I = 0
            HASH = 0
            continue
        #Checks last three bits of hash
        elif HASH & 0x7 == 0:
            breakindices.append(num)
            I = 0
            HASH = 0


    outputfile = open("FastOutput", 'w')
    for i in breakindices:
        outputfile.write("%s\n" % i)
    outputfile.close()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        src = sys.argv[1] # data buffer
        main(src)
    else:
        print("Usage: fastcdc.py <databuffer>")