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
    # plt.axis([1,5, 0, 1.6])

    print(timeL)
    # timeL = [timeL[0]]
    plt.axis([1,5,0, 25])

    for test in timeL:
        print(test)
        #Graphing strong scaling
        # newResult = [float(test[1][0][1])/ float(timing[1])/ int(timing[0]) for timing in test[1]]
        # print(newResult)
        newResult = [(float(timing[1])) for timing in test[1]]
        newResult = [0] + newResult
        print(newResult)
        print(test[0])

        plt.plot(newResult, linewidth = 2.0, label = test[0])
    # plt.legend(bbox_to_anchor=(1.05, 1), loc=3, borderaxespad=0.)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=4,
           ncol=1, borderaxespad=0.)
    plt.xlabel("Problem Scale")
    plt.ylabel('Runtime (s)')
    SIZE = 25
    bigSize = 50
    plt.rc('font', size=SIZE)  # controls default text sizes
    plt.rc('axes', titlesize=500)  # fontsize of the axes title
    plt.rc('axes', labelsize=500)  # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SIZE)  # fontsize of the tick labels
    plt.rc('ytick', labelsize=SIZE)  # fontsize of the tick labels
    plt.rc('legend', fontsize=SIZE)  # legend fontsize
    plt.rc('figure', titlesize=SIZE * 2)  # fontsize of the figure title
    plt.show()
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



    plt.title("Strong Scaling Efficiency vs Number of Processes")

    plt.axis([1,5, 0, 200])
    for timeResult in timeL:
        # print(timeResult)
        # print(timeResult[1][0][0])

        #Scaling Efficiency Graph
        # newResult = [[float(timeResult[1][0][1])/(float(timing[1]) *float(timing[0]))] for timing in timeResult[1]]
        # newResult = [[0]] + newResult

        #For percentage graph
        # newResult = [[float(timing[1])/float(timeResult[1][0][1] *)] for timing in timeResult[1]]
        # newResult =  newResult
        # newResult = [[0]] + newResult   

        #Sqrt magnitude plot
        newResult = [[float(timing[1])] for timing in timeResult[1]]
        newResult =  newResult
        newResult = [[0]] + newResult
        # if timeResult[0] == 'allhomes' or timeResult[0] == 'homes1212' or timeResult[0] == 'bighomes100':
        plt.plot(newResult, linewidth = 2.0, label = timeResult[0])
        plt.legend(bbox_to_anchor=(1.005, 0., 1., .102), loc=3,
               ncol=1, borderaxespad=0.)

        plt.xlabel("Number of Processors")
        plt.ylabel("Scaling Efficiency")    
        #log graph
        # newResult = [[math.log(float(timing[1]))] for timing in timeResult[1]]
        # newResult = [[0]] + newResult
        # plt.plot(newResult, linewidth = 2.0)

        #print(newResult)
        # For real time plots
        #newResult = [[float(timing[1])] for timing in timeResult[1]]

        #plt.plot(timingResult[1], linewidth = 2.0)
    SIZE = 25
    bigSize = 50
    plt.rc('font', size=SIZE)  # controls default text sizes
    plt.rc('axes', titlesize=500)  # fontsize of the axes title
    plt.rc('axes', labelsize=500)  # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SIZE)  # fontsize of the tick labels
    plt.rc('ytick', labelsize=SIZE)  # fontsize of the tick labels
    plt.rc('legend', fontsize=10)  # legend fontsize
    plt.rc('figure', titlesize=SIZE * 2)  # fontsize of the figure title
    plt.show()


if __name__ == '__main__':
    main()