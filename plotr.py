import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import datetime as DT
import matplotlib.dates as mdates
import scipy

data= np.loadtxt('data2.csv', delimiter=',',
         dtype={'names': ('date', 'session'),'formats': ('S10', 'i4')} )

#Organizes 2-column spreadsheet
dates, sessions = map(list, zip(*data))
print dates, sessions

x = [DT.datetime.strptime(date,"%m-%d-%y") for date in dates]
y = [sessions]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.xaxis_date()
ax.grid()
#Fills space under plotted line
ax.fill_between(x, sessions, color='blue')

# slants the x axis
fig.autofmt_xdate()
plt.plot(x,sessions)
plt.xlabel('Date')
plt.ylabel('Sessions')
plt.title('Peak Usage')


savefig('graph.png')
