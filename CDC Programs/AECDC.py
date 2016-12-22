'''
This is a python implementation of AECDC.
Author: Kanishk Tantia, Jason Ma
Date:  December 3rd, 2016
'''

import sys
window = 8
interval = 8

def AEChunk(LBAlist):
	L = len(LBAlist)
	i = 0
	global window
	for i in range(0,L-i-1-window):
		if LBAlist[i] >= max(LBAlist[:i+1+window]):
			if max(LBAlist[:i]) < LBAlist[i]:
				return i
	return L

def main(src):
    '''
    Input: data buffer src
    '''
    target = open(src, 'r')

    LBAlist = target.readlines()

    breakindices = []

    prev = 0

    while len(LBAlist) > window:
    	x = AEChunk(LBAlist)
    	breakindices.append(x + prev)
    	prev = x + prev
    	if x + 1 > len(LBAlist):
    		break
    	LBAlist = LBAlist[x+1:]

    outputfile = open("AEOutput", 'w')
    for i in breakindices:
        outputfile.write("%s\n" % i)
    outputfile.close()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        src = sys.argv[1] # data buffer
        main(src)
    else:
        print "Usage: AECDC.py <databuffer>"