import scipy.stats
import math
import matplotlib.pyplot as plt
import random
import numpy




def computeVar(v0, r):

    ##Basic calculation of VaR

    v1=v0*(math.exp(r))
    var=v0-v1
    return var


def normProb(mean, sd,percentile):
    ##percent point function, returns x for given percentile
    return scipy.stats.norm.ppf(percentile, mean, sd)



def plotHistogram(x):

    ##Plots Histogram for data with 50 bins, values of each point are weighted by 1/n to display probability on y-axis

    plt.hist(x,50,weights=numpy.ones(len(x))/len(x))
    plt.ylabel('Probability')
    plt.xlabel('P/L in millions')
    plt.show()

    return 0




def main():

    ##Given a certain portfolio value and standard deviation to return, simulates returns according
    ##to a normal distribution and returns results in the form of a histogram.

    print('Input your initial portfolio value v0 in millions:')
    marketVal = int(input())
    print('Input the standard deviation of your return:')
    standardDev = float(input())
    print('Input the mean of your return:')
    mean = float(input())

    data = numpy.zeros(1000000)

    for x in range(0,1000000):
        data[x]=computeVar(marketVal,numpy.random.normal(mean,standardDev))*(-1)

    plotHistogram(data)


main()









