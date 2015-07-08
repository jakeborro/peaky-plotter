import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import datetime as DT
import plotly.plotly as py

data= np.loadtxt('daily_count.csv', delimiter=',',
         dtype={'names': ('date', 'time'),'formats': ('S10', 'S10')} )

dates, times = map(list, zip(*data))
print dates, times

x = [DT.datetime.strptime(date,"%m-%d-%y") for date in dates]
y = [DT.datetime.strptime(time,"%H:%M") for time in times]


fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid()


plt.plot(x,y)
plt.xlabel('Date')
plt.ylabel('Time')
plt.title('Peak Time')



savefig('graph.png')
