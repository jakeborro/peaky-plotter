#!/usr/bin/python

import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import datetime as DT
import matplotlib.dates as mdates
import glob


def main():
  files = glob.glob('./*.history.csv')

  for file in files:
    data = np.loadtxt(file, delimiter=',', dtype={'names': ('date', 'session'),'formats': ('S10', 'i4')} )

    #Organizes 2-column spreadsheet
    dates, sessions = map(list, zip(*data))
    print dates, sessions

    x = [DT.datetime.strptime(date,"%m-%d-%y") for date in dates]
    y = [sessions]

    fig = plt.figure()
    axis = fig.add_subplot(111)
    axis.xaxis_date()
    axis.grid()
    #Fills space under plotted line
    axis.fill_between(x, sessions, color='blue')

    # slants the x axis
    fig.autofmt_xdate()
    plt.plot(x,sessions)
    plt.xlabel('Date')
    plt.ylabel('Sessions')
    plt.title('Peak Usage')

    savefig(file + '.png')

main()
