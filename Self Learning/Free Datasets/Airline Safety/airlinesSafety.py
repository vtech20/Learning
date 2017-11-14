# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 19:34:47 2017

@author: baradhwaj
"""
import os
import numpy as np
import pandas as pd

os.getcwd()
os.chdir("G:\Python\Learning\Self Learning\Free Datasets\Airline Safety\ " )
airlineSafety = pd.read_csv("airline-safety.csv",thousands =',')
print(airlineSafety)

#Q1 . Which flight has maximum occupancy
cond1 = np.max(airlineSafety['avail_seat_km_per_week'])
maxRow = airlineSafety[airlineSafety['avail_seat_km_per_week']==cond1]
print(maxRow['airline'])

#Q2.Which  3 flight has least fatalities with maximum occuapcy

occupancySorted = airlineSafety.sort(['avail_seat_km_per_week'], ascending=[0])
print(occupancySorted)
leastFatalData8599 = occupancySorted.sort(['fatalities_85_99'],ascending=1)
 #f0 = airlineSafety.groupby('').head(3)
foo = airlineSafety['fatalities_85_99'].sort().unique()
print(foo)


#Q1. * Top 5 airlines which has maximum deaths in 85-99 
mostDeathCond = airlineSafety.sort(['fatalities_85_99'],ascending=0).head(5)
print(mostDeathCond['airline'])

#* Compare the percentage of incidents of United / Continental airlines 
#between 85-99 and 2000 - 2014  - is it scatter plot ?
# need a column with repeating values to display box plot comparision?!!

print(np.mean(airlineSafety['incidents_00_14']))
#airlineSafety.loc['',]
#airlineSafety.boxplot(column="incidents_85_99",by="airline")
#* Compare the percentage of fatalities of Aeroflot airlines between 85-99 and 2000 - 2014 
#* Which airlines is having the highest percentage of deaths increased between 85-99 and 2000 - 2014 
fatalityDiff = airlineSafety['fatalities_85_99'] - airlineSafety['fatalities_00_14']
airlineSafety['diffFatality'] = (fatalityDiff  / airlineSafety['fatalities_85_99'])
mostDeathList = airlineSafety.sort(['diffFatality'],ascending=1).head(1)
print(mostDeathList['airline'])

# * Which airlines is having the highest (first among the airlines greater than average incident)
# average incident happen between 85 and 99  - Can b done without taking avg too
avg_inc8599 = np.mean(airlineSafety['incidents_85_99'])
grAvg  = airlineSafety['incidents_85_99'] > avg_inc8599
print(airlineSafety.loc[grAvg ,['airline']])

 print(airlineSafety.loc[airlineSafety['incidents_85_99'] == np.max(airlineSafety['incidents_85_99']),'airline'])