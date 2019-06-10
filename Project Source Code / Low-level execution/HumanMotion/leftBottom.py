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
for i in range(3):
        for m in range(3):
            arr.append(HIGHTARR[2])
print arr

leftBottom=pd.read_csv('leftBottom.csv')
#print leftThree.loc[0:, 'RhipX':'RhipZ' ]

name=['RhipX','Lhip','Lshoulder','HLelbow','Lelbow','Lhand','Rshoulder','HRelbow','Relbow','Rhand','Lfeet','Lknee',
      'Lwaist','Rwaist','Rknee','Rfeet']
openpose=leftBottom.ix[[110,111,112,409,410,411,669,670,671],0:] #opening data
openpose['height']=arr
openpose=openpose.replace(0, np.nan)

opening=leftBottom.ix[[132,133,134,436,437,438,706,707,708],0:] #opening
opening['height']=arr
opening=opening.replace(0, np.nan)

close=leftBottom.ix[[175,176,177,458,459,460,751,752,753],0:] #close
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
#frame 112 [column 111] bottom hight ----1st time ---open pose
#frame 411 [column 410] bottom hight ----2st time ---open pose
#frame 671 [column 670] bottom hight ----3st time ---open pose

print '\n'
print 'bottom, left hand "start to open" pose:\n'
print '\n'

count=1
for j in range(16):
    print '\n'
    print 'the prediction coordinate of ',name[j],":\n",
    opencoordinate(count, count+3)
    count=(j+1)*3+1


#frame 134 [column 133] bottom hight ----1st time ---opening
#frame 438 [column 437] bottom hight ----2st time ---opening
#frame 708 [column 707] bottom hight ----3st time ---opening
print '\n'
print 'bottom, left hand opening pose:\n'
print '\n'

count1=1
for j in range(16):
    print '\n'
    print 'the prediction coordinate of ',name[j],":\n",
    openingcoordinate(count1, count1+3)
    count1=(j+1)*3+1


#frame 177 [column 176] bottom hight ----1st time ---close
#frame 460 [column 459] bottom hight ----2st time ---close
#frame 753 [column 752] bottom hight ----3st time ---close
print '\n'
print 'bottom, left hand close pose:\n'
print '\n'

count2=1
for j in range(16):
    print '\n'
    print 'the prediction coordinate of ',name[j],":\n",
    closecoordinate(count2, count2+3)
    count2=(j+1)*3+1