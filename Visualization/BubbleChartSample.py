# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 22:21:12 2015

@author: ItelinaMa
"""

from pylab import *
from scipy import *

# reading the data from a csv file
durl = 'http://datasets.flowingdata.com/crimeRatesByState2005.csv'
rdata = genfromtxt(durl,dtype='S8,f,f,f,f,f,f,f,i',delimiter=',')

rdata[0] = zeros(8) # cutting the label's titles
rdata[1] = zeros(8) # cutting the global statistics

x = []
y = []
color = []
area = []

for data in rdata:
 x.append(data[1]) # murder
 y.append(data[5]) # burglary
 color.append(data[6]) # larceny_theft 
 area.append(sqrt(data[8])) # population
 # plotting the first eigth letters of the state's name
 text(data[1], data[5], 
      data[0],size=11,horizontalalignment='center')

# making the scatter plot
sct = scatter(x, y, c=color, s=area, linewidths=2, edgecolor='w')
sct.set_alpha(0.75)

axis([0,11,200,1280])
xlabel('Murders per 100,000 population')
ylabel('Burglaries per 100,000 population')
show()