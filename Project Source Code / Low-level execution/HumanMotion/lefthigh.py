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
HIGHEST=91
arr = []
MYHIGHT = 40.5

#each hight try three times
for i in range(3):
        for m in range(3):
            arr.append(HIGHEST)
print arr

lefthigh=pd.read_csv('lefthigh.csv')
#print leftThree.loc[0:, 'RhipX':'RhipZ' ]

name=['RhipX','Lhip','Lshoulder','HLelbow','Lelbow','Lhand','Rshoulder','HRelbow','Relbow','Rhand','Lfeet','Lknee',
      'Lwaist','Rwaist','Rknee','Rfeet']
openpose=lefthigh.ix[[122,123,124,369,370,371,604,605,606],0:] #opening data
openpose['height']=arr
openpose=openpose.replace(0, np.nan)

opening=lefthigh.ix[[161,162,163,406,407,408,640,641,642],0:] #opening
opening['height']=arr
opening=opening.replace(0, np.nan)

close=lefthigh.ix[[201,202,203,450,451,452,677,678,679],0:] #close
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
#frame 274 [column 273-150=123] bottom hight ----1st time ---open pose
#frame 521 [column 520-150=370] bottom hight ----2st time ---open pose
#frame 756 [column 755-150=605] bottom hight ----3st time ---open pose

print '\n'
print 'highest, left hand "start to open" pose:\n'
print '\n'

count=1
for j in range(16):
    print '\n'
    print 'the prediction coordinate of ',name[j],":\n",
    opencoordinate(count, count+3)
    count=(j+1)*3+1


#frame 313 [column 312-150=162] bottom hight ----1st time ---opening
#frame 558 [column 557-150=407] bottom hight ----2st time ---opening
#frame 792 [column 791-150=641] bottom hight ----3st time ---opening
print '\n'
print 'highest, left hand opening pose:\n'
print '\n'

count1=1
for j in range(16):
    print '\n'
    print 'the prediction coordinate of ',name[j],":\n",
    openingcoordinate(count1, count1+3)
    count1=(j+1)*3+1


#frame 353 [column 352-150=202] bottom hight ----1st time ---close
#frame 602 [column 601-150=451] bottom hight ----2st time ---close
#frame 829 [column 828-150=678] bottom hight ----3st time ---close
print '\n'
print 'highest, left hand close pose:\n'
print '\n'

count2=1
for j in range(16):
    print '\n'
    print 'the prediction coordinate of ',name[j],":\n",
    closecoordinate(count2, count2+3)
    count2=(j+1)*3+1