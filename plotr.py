import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import datetime as DT
import matplotlib.dates as mdates
import scipy
import os
import glob

rootdir='/path/to/file'

for infile in glob.glob( os.rootdir.join(rootdir, '*.history.csv.out') ):
    output = infile + '.out'

data= np.loadtxt(infile, delimiter=',',
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

fileNameTemplate = r'\path\to\file\Plot{}.png'

for subdir,dirs,files in os.walk(rootdir):
    for count, file in enumerate(files):
        # Generate a plot in `pl`
        pl.savefig(fileNameTemplate.format(count), format='png')
        pl.clf()  # Clear the figure for the next loop
