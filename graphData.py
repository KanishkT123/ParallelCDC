import time
import matplotlib.pyplot as plt
import math


def main():
    with open('ProblemScaling.txt', 'r+') as f:
        lines = f.readlines()
        timeL = []
        for i in range(0,len(lines),2):
            times = lines[i + 1].split(' ')
            times = [[int(time) + 1,times[time]] for time in range(len(times)) if '\n' not in times[time]]
            timeL += [[lines[i].replace('\n',''), times]]
    plt.title("Weak Scaling Test")
    print(timeL)
    # plt.axis([1,5,0, 25])

    for test in timeL:
        print(test)
        #Graphing strong scaling
        newResult = [float(test[1][0][1])/ float(timing[1]) for timing in test[1]]
        # print(newResult)
        # newResult = [(float(timing[1])) for timing in test[1]]
        newResult = [0] + newResult
        print(newResult)
        print(test[0])

        plt.plot(newResult, linewidth = 2.0, label = test[0])
    # plt.legend(bbox_to_anchor=(1.05, 1), loc=3, borderaxespad=0.)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=4,
           ncol=1, borderaxespad=0.)
    plt.xlabel("Problem Scale")
    plt.ylabel('Runtime (s)')
    plt.show()



def main2():
    with open('ProcessorTimesFinal.txt', 'r+') as f:
        lines = f.readlines()
        timeL = []
        for i in range(0,len(lines),2):
            times = lines[i + 1].split(' ')
            times = [[int(time) + 1,times[time]] for time in range(len(times)) if '\n' not in times[time]]
            timeL += [[lines[i].replace('\n',''), times]]
    #print(timeL)

    print(timeL)
    plt.title("Strong Scaling Efficiency vs Number of Processes")
    plt.axis([1,5, 0, 1.6])
    for timeResult in timeL:
        # print(timeResult)
        # print(timeResult[1][0][0])

        #Scaling Efficiency Graph
        newResult = [[float(timeResult[1][0][1])/(float(timing[1]) *float(timing[0]))] for timing in timeResult[1]]
        newResult = [[0]] + newResult

        #For percentage graph
        # newResult = [[float(timing[1])/float(timeResult[1][0][1] *)] for timing in timeResult[1]]
        # newResult =  newResult
        # newResult = [[0]] + newResult   

        #Sqrt magnitude plot
        # newResult = [[math.sqrt(float(timing[1]))] for timing in timeResult[1]]
        # newResult =  newResult
        # newResult = [[0]] + newResult
        if timeResult[0] == 'allhomes' or timeResult[0] == 'homes17' or timeResult[0] == 'homes18':
            plt.plot(newResult, linewidth = 2.0, label = timeResult[0])
        plt.legend(bbox_to_anchor=(1.02, 0., 1.5, .102), loc=3,
               ncol=1, borderaxespad=0.)

        plt.xlabel("Number of Processors")
        plt.ylabel("Strong Scaling Efficiency")    
        #log graph
        # newResult = [[math.log(float(timing[1]))] for timing in timeResult[1]]
        # newResult = [[0]] + newResult
        # plt.plot(newResult, linewidth = 2.0)

        #print(newResult)
        # For real time plots
        #newResult = [[float(timing[1])] for timing in timeResult[1]]

        #plt.plot(timingResult[1], linewidth = 2.0)
    plt.show()


if __name__ == '__main__':
    main2()