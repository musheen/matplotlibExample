import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator,FormatStrFormatter
import sys


# Import data and read from text
#
# Data is from an MMS study I ran. 
#
data1 = np.genfromtxt('error.sst.com.dat',names=('h1','r1','ru1','rv1','re1','rk1','ro1'),dtype=float)
data2 = np.genfromtxt('error.sst.inv.dat',names=('h2','r2','ru2','rv2','re2','rk2','ro2'),dtype=float)
data3 = np.genfromtxt('error.sst.vis.dat',names=('h3','r3','ru3','rv3','re3','rk3','ro3'),dtype=float)


# Importing the data from the first file
#
h1  = data1['h1']
r1  = data1['r1']
ru1 = data1['ru1']
rv1 = data1['rv1']
re1 = data1['re1']
rk1 = data1['rk1']
ro1 = data1['ro1']

# Importing the data from the second file
#
h2  = data2['h2']
r2  = data2['r2']
ru2 = data2['ru2']
rv2 = data2['rv2']
re2 = data2['re2']
rk2 = data2['rk2']
ro2 = data2['ro2']

# Importing the data from the third file
#
h3  = data3['h3']
r3  = data3['r3']
ru3 = data3['ru3']
rv3 = data3['rv3']
re3 = data3['re3']
rk3 = data3['rk3']
ro3 = data3['ro3']

# Creating arrays for use later
#
x1 = []
y1 = []
#
# Filling in the arrays with data
#
x1.append(h1[2])
x1.append(h1[3])
x1.append(h1[3])
y1.append(ru1[2])
y1.append(ru1[2])
y1.append(ru1[3])


x2 = []
y2 = []
x2.append(h2[0])
x2.append(h2[1])
x2.append(h2[1])
y2.append(ru2[0])
y2.append(ru2[0])
y2.append(ru2[1])


x3 = []
y3 = []
x3.append(h3[2])
x3.append(h3[3])
x3.append(h3[3])
y3.append(ru3[2])
y3.append(ru3[2])
y3.append(ru3[3])


minorLocator   = MultipleLocator(100)


# plot here
fig = plt.figure(1)
ax = fig.add_subplot(111)
#
#

# Plotting each of the data sets
#
# h1 is the x axis data
# ru1 is the y axis data
# - is the line style
# o is the marker style 
# k is the color (black)
#
# This is all customizeable to preference
#
ax.plot(h1,ru1,'-ok')
ax.plot(h2,ru2,'--ok')
ax.plot(h3,ru3,'-.ok')
#



# This part is a little tricky, and really only used for MMS, but its nice to have
# What I am doing here is creating a right angle triangle to show the slope.
#
# This part is very dependent on the data, so a lot of trial and error is needed to make it
# look right.
#
#
ax.plot(x1,y1,'-k',linewidth=0.3)


# Here I am annotating the slope with an order of accuracy. 
# The x and y coordinates are the location of the text, and the 3.0 is the text.
#
ax.text(h1[3]*1.01,(ru1[2]-ru1[3])/2*0.625, r'3.0', fontsize=20)


#
# Here, I am annotating the data with an arrow (arrow head set to zero to make a nice 
# looking line) and the line information.
#
# I would not reccomend using the arrow because it changes size way too much.
#
# A legend could just as easily be used instead, but sometimes this looks better.
#
#
ax.annotate('Re = 100,000',fontsize='20', xy=(h1[3],ru1[3]), 
            xytext=(100, 1E-8),
            arrowprops=dict(facecolor='black', shrink=0.1,width=0.01,headwidth=0))


ax.plot(x2,y2,'-k',linewidth=0.3)
ax.text(h2[1]*1.01,(ru2[0]-ru2[1])/2*.7, r'3.0', fontsize=20)

ax.annotate('Inviscid Only',fontsize='20', xy=(h2[1],ru2[1]), 
            xytext=(20, 1E-5),
            arrowprops=dict(facecolor='black', shrink=0.1,width=0.01,headwidth=0))



ax.plot(x3,y3,'-k',linewidth=0.3)
ax.text(h3[3]*1.01,(ru3[2]-ru3[3])/2*0.5, r'4.1', fontsize=20)

ax.annotate('Viscous Only',fontsize='20', xy=(h3[2],ru3[2]), 
            xytext=(20, 1E-11),
            arrowprops=dict(facecolor='black', shrink=0.1,width=0.01,headwidth=0))


# Set the x and y scale as log scales
#
ax.set_yscale('log')
ax.set_xscale('log')
#

# Set the x and y limit on the graph to maximise the space
#
ax.set_xlim((18,300))
ax.set_ylim((1E-12,1E-3))
#

# Legend can be used here instead. Try use this an see how it looks. 
# You can comment out the annotations if theyre in the way.
#
# numpoints=1 sets only 1 point in the legend - default is two and is ugly
# 
# loc gives the location of the legend. Its really simple. 
# Upper right puts in the legend in the upper right.
#
#plt.legend(('Combined','Inviscid Only','Viscous Only'),loc="upper right",prop={'size':18},numpoints=1).draw_frame(False)
#


# Remove the right and top lines around the box to make it better looking 
# 
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
#


# x and y axis label - needs to be big for journals
#
ax.set_ylabel(('RMS Error (x-momentum)'),fontsize="24",weight='bold')
ax.set_xlabel(('1/h'),fontsize="24",weight='bold')
#
# If you want to use LaTex in the label, use '$\mathregular{your text here}$'
#

# Remove useless ticks to make the graph look better
#
ax.tick_params(axis='x',which='minor',bottom='off',top='off')
ax.tick_params(axis='y',which='minor',left='off',right='off')
ax.tick_params(axis='x',which='major',top='off')
ax.tick_params(axis='y',which='major',right='off')
ax.xaxis.set_tick_params(width=1.5,length=8)
ax.yaxis.set_tick_params(width=1.5,length=8)
#
for axis in ['bottom','left']:
  ax.spines[axis].set_linewidth(1.5)
#

# In order to get better looking plot, I add which ticks I want myself. 
# This allows me to keep cartjunk to a minimum and make things look the way I want.
#
ax.yaxis.set_ticks([1E-4,1E-6,1E-8,1E-10,1E-12])
ax.set_yticklabels(["$\mathregular{10^{-4}}$","$\mathregular{10^{-6}}$","$\mathregular{10^{-8}}$","$\mathregular{10^{-10}}$","$\mathregular{10^{-12}}$"],fontsize="14")

#
ax.xaxis.set_ticks([100,200,300])
ax.set_xticklabels(["100", "200", "300","400"],fontsize="14")

# Show the plot
#
plt.show()


