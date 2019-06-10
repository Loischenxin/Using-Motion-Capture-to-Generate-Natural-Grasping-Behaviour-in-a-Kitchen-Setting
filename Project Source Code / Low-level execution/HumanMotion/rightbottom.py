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

rightBottomn=pd.read_csv('rightbottom.csv')
#print leftThree.loc[0:, 'RhipX':'RhipZ' ]

name=['RhipX','Lhip','Lshoulder','HLelbow','Lelbow','Lhand','Rshoulder','HRelbow','Relbow','Rhand','Lfeet','Lknee',
      'Lwaist','Rwaist','Rknee','Rfeet']
openpose=rightBottomn.ix[[131,132,133,348,349,350,600,601,602],0:] #opening data
openpose['height']=arr
openpose=openpose.replace(0, np.nan)

opening=rightBottomn.ix[[159,160,161,377,378,379,627,628,629],0:] #opening
opening['height']=arr
opening=opening.replace(0, np.nan)

close=rightBottomn.ix[[186,187,188,403,404,405,659,660,661],0:] #close
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
#frame 283 [column 282-150=132] bottom hight ----1st time ---open pose
#frame 500 [column 499-150=349] bottom hight ----2st time ---open pose
#frame 752 [column 751-150=601] bottom hight ----3st time ---open pose

print '\n'
print 'bottom, right hand "start to open" pose:\n'
print '\n'

count=1
for j in range(16):
    print '\n'
    print 'the prediction coordinate of ',name[j],":\n",
    opencoordinate(count, count+3)
    count=(j+1)*3+1


#frame 311 [column 310-150=160] bottom hight ----1st time ---opening
#frame 529 [column 528-150=378] bottom hight ----2st time ---opening
#frame 779 [column 778-150=628] bottom hight ----3st time ---opening
print '\n'
print 'bottom, right hand opening pose:\n'
print '\n'

count1=1
for j in range(16):
    print '\n'
    print 'the prediction coordinate of ',name[j],":\n",
    openingcoordinate(count1, count1+3)
    count1=(j+1)*3+1


#frame 338 [column 337-150=187] bottom hight ----1st time ---close
#frame 555 [column 554-150=404] bottom hight ----2st time ---close
#frame 811 [column 810-150=660] bottom hight ----3st time ---close
print '\n'
print 'bottom, right hand close pose:\n'
print '\n'

count2=1
for j in range(16):
    print '\n'
    print 'the prediction coordinate of ',name[j],":\n",
    closecoordinate(count2, count2+3)
    count2=(j+1)*3+1