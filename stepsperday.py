#!/usr/bin/env python3

from matplotlib import pyplot as plt
from matplotlib import dates
from datetime import date

dow = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

if __name__ == "__main__":

    fd = open('Export.csv','r')
    datelist = []
    steps    = []
    lines    = fd.readlines()
    for line in lines[1:]:              
        a = line.rstrip().split(',')    
        datelist.append(a[0])           



    tmp = list(map(dates.datestr2num, datelist))


    xdate = list(map(dates.num2date, tmp))


    tmp = list(map(date.weekday, xdate))          


    ticks = list(map(lambda t: dow[t], tmp))      

    plt.style.use('ggplot')

    plt.figure(figsize=(16,9), dpi=100)     
    plt.title('Steps Per Day While Carrying iPhone',fontsize=28)
    plt.ylabel('Number of Steps',fontsize=16)

    plt.bar(xdate,steps)                    
    plt.xticks(xdate, ticks, rotation=45)   
    plt.show()

