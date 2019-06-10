import csv
import numpy as np
from math import *
import pandas as pd
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
from sklearn import linear_model

HIGHT=47.5

BOTTOM=30
MIDDLE=45
TOP=60
HIGHTARR = [TOP,MIDDLE,BOTTOM]
arr = []
MYHIGHT = 40.5

#each hight try three times

for j in HIGHTARR:
    for m in range(9):
        arr.append(j)
print arr

rightThree=pd.read_csv('right3hight.csv')
#print leftThree.loc[0:, 'RhipX':'RhipZ' ]

name=['RhipX','Lhip','Lshoulder','HLelbow','Lelbow','Lhand','Rshoulder','HRelbow','Relbow','Rhand','Lfeet','Lknee',
      'Lwaist','Rwaist','Rknee','Rfeet']
openpose=rightThree.ix[[152,153,154,437,438,439,694,695,696,956,957,958,1240,1241,1242,
                       1525,1526,1527,1771,1772,1773,2010,2011,2012,2258,2259,2260],0:] #opening data
openpose['height']=arr
openpose=openpose.replace(0, np.nan)

opening=rightThree.ix[[195,196,197,480,481,482,718,719,720,990,991,992,1276,1277,1278,
                      1556,1557,1558,1798,1799,1800,2033,2034,2035,2279,2280,2281],0:] #opening
opening['height']=arr
opening=opening.replace(0, np.nan)

close=rightThree.ix[[227,228,229,514,515,516,755,756,757,1033,1034,1035,1312,1313,1314,
                    1587,1588,1589,1820,1821,1822,2080,2081,2082,2318,2319,2320],0:] #close
close['height']=arr
close=close.replace(0, np.nan)

#print openpose
#print opening
#print close

#build regression model ---linear regression
linreg=linear_model.LinearRegression()

def opencoordinate(x,y):

    for i in range(x, y):
        nona = openpose.iloc[0:, [i, 49]].dropna()
        if nona.empty:
            print 'no coordinate'
            break
        linreg.fit(nona['height'].values.reshape(-1, 1), nona.iloc[:, [0]])  # because Rhip has one dimension
        #a, b = linreg.coef_, linreg.intercept_

        myheight= np.array(MYHIGHT).reshape(-1, 1)
        print linreg.predict(myheight)

def openingcoordinate(x,y):

    for i in range(x, y):
        nona = opening.iloc[0:, [i, 49]].dropna()
        if nona.empty:
            print 'no coordinate'
            break
        linreg.fit(nona['height'].values.reshape(-1, 1), nona.iloc[:, [0]])  # because Rhip has one dimension
        #a, b = linreg.coef_, linreg.intercept_

        myheight= np.array(MYHIGHT).reshape(-1, 1)
        print linreg.predict(myheight)


def closecoordinate(x,y):

    for i in range(x, y):
        nona = close.iloc[0:, [i, 49]].dropna()
        if nona.empty:
            print 'no coordinate'
            break
        linreg.fit(nona['height'].values.reshape(-1, 1), nona.iloc[:, [0]])  # because Rhip has one dimension
        #a, b = linreg.coef_, linreg.intercept_

        myheight= np.array(MYHIGHT).reshape(-1, 1)
        print linreg.predict(myheight)

################left3higt###################### left hand
#frame 154 [column 153] top hight ----1st time ---open pose
#frame 439 [column 438] top hight ----2st time ---open pose
#frame 694 [column 693] top hight ----3st time ---open pose
#frame 957 [column 956] middle hight ----1st time ---open pose
#frame 1241 [column 1240] middle hight ----2st time ---open pose
#frame 1526 [column 1525] middle hight ----3st time ---open pose
#frame 1772 [column 1771] bottom hight ----1st time ---open pose
#frame 2011 [column 2010] bottom hight ----2st time ---open pose
#frame 2259 [column 2258] bottom hight ----3st time ---open pose

print '\n'
print 'right hand "start to open" pose:\n'
print '\n'

count=1
for j in range(16):
    print '\n'
    print 'the prediction coordinate of ',name[j],":\n",
    opencoordinate(count, count+3)
    count=(j+1)*3+1

#frame 196 [column 195] top hight ----1st time ---opening
#frame 481 [column 480] top hight ----2st time ---opening
#frame 719 [column 718] top hight ----3st time ---opening
#frame 991 [column 990] middle hight ----1st time ---opening
#frame 1277 [column 1276] middle hight ----2st time ---opening
#frame 1557 [column 1556] middle hight ----3st time ---opening
#frame 1799 [column 1798] bottom hight ----1st time ---opening
#frame 2034 [column 2033] bottom hight ----2st time ---opening
#frame 2280 [column 2279] bottom hight ----3st time ---opening
print '\n'
print 'right hand opening pose:\n'
print '\n'

count1=1
for j in range(16):
    print '\n'
    print 'the prediction coordinate of ',name[j],":\n",
    openingcoordinate(count1, count1+3)
    count1=(j+1)*3+1

#frame 228 [column 227] top hight ----1st time ---close
#frame 515 [column 514] top hight ----2st time ---close
#frame 756 [column 755] top hight ----3st time ---close
#frame 1034 [column 1033] middle hight ----1st time ---close
#frame 1313 [column 1312] middle hight ----2st time ---close
#frame 1588 [column 1587] middle hight ----3st time ---close
#frame 1821 [column 1820] bottom hight ----1st time ---close
#frame 2081 [column 2080] bottom hight ----2st time ---close
#frame 2319 [column 2318] bottom hight ----3st time ---close
print '\n'
print 'right hand close pose:\n'
print '\n'

count2=1
for j in range(16):
    print '\n'
    print 'the prediction coordinate of ',name[j],":\n",
    closecoordinate(count2, count2+3)
    count2=(j+1)*3+1