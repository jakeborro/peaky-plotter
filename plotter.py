#!/usr/bin/python

import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import datetime as DT
import matplotlib.dates as mdates
import glob


def main():
  files = glob.glob('./*.csv')

  for file in files:
    data = np.loadtxt(file, delimiter=',', dtype={'names': ('date', 'session'),'formats': ('S10', 'i4')} )

    dates, sessions = map(list, zip(*data))
    print dates, sessions

    x = [DT.datetime.strptime(date,"%m-%d-%y") for date in dates]
    y = [sessions]

    fig = plt.figure()
    axis = fig.add_subplot(111)
    axis.xaxis_date()
    axis.grid()
    #Fills space under plotted line with specified color
    axis.fill_between(x, sessions, color='blue')

    #Slants the x axisfor aesthetics
    fig.autofmt_xdate()
    plt.plot(x,sessions)
    plt.xlabel('Date')
    plt.ylabel('Sessions')
    plt.title('Peak Usage')

    savefig(file + '.png')

main()
