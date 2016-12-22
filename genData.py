import random
import sys
import time
def genDataset(src, N, newDataSize):
    random.seed(time.time())
    lines = open(src, 'r+').readlines()
    # setOfSets = []
    # for a in range(N + 1):
    #     setOfSets.append([])
    # print(setOfSets)
    # for i in range(len(lines)):
    #     if i % 100000 == 0:
    #         print(i)
    #     for b in range(2,N + 1):
    #         newSet = lines[i:i + b ]
    #         # For speed requirements, we left out this if statement
    #         # Just need to assemble a list of possible sequences to write
    #         #if newSet not in setOfSets[b]:
    #         setOfSets[b].append(newSet)
    # #print(setOfSets)
    # print(len(setOfSets))
    f = open('dummy.txt', 'w+')
    #print(setOfSets)
    print("Now starting file generation")
    fileLength = len(lines)
    count = 0
    num = [0 for x in range(N + 1)]
    while (count < newDataSize):
        if count % 1000000 == 0:
            print("Currently at line {0}".format(count))
        size = int(random.random() * (N * 0.99) + 1)
        num[size] += 1
        startIndex = int(random.random() * fileLength)
        if size < 1 or size > N:
            print("REEEE")
        #print(size)
        else:
            writeData = lines[startIndex:startIndex + size]
            for data in writeData:
                f.write(str(data))
            count += size
    f.close()
    print(num)





if __name__ == '__main__':
    if len(sys.argv) == 4:
        src = sys.argv[1] # data buffer
        complexity = int(sys.argv[2])
        dataSize = int(sys.argv[3])
        # print(src)
        # print(complexity)
        # print(dataSize)
        genDataset(src, complexity, dataSize)
    else:
        print("Usage: fastcdc.py <databuffer>")