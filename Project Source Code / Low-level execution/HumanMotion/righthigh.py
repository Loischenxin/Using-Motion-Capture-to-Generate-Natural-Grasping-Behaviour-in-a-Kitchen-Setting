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
HIGHEST=91
HIGHTARR = [TOP,MIDDLE,BOTTOM]
arr = []
MYHEIGHT = 56

#each hight try three times
for i in range(3):
        for m in range(3):
            arr.append(HIGHEST)
print arr

righthigh=pd.read_csv('righthigh.csv')
#print leftThree.loc[0:, 'RhipX':'RhipZ' ]

name=['RhipX','Lhip','Lshoulder','HLelbow','Lelbow','Lhand','Rshoulder','HRelbow','Relbow','Rhand','Lfeet','Lknee',
      'Lwaist','Rwaist','Rknee','Rfeet']
openpose=righthigh.ix[[113,114,115,312,313,314,529,530,531],0:] #opening data
openpose['height']=arr
openpose=openpose.replace(0, np.nan)

opening=righthigh.ix[[143,144,145,334,335,336,554,555,556],0:] #opening
opening['height']=arr
opening=opening.replace(0, np.nan)

close=righthigh.ix[[171,172,173,364,365,366,586,587,588],0:] #close
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

        myheight= np.array(MYHEIGHT).reshape(-1, 1)
        print linreg.predict(myheight)

def openingcoordinate(x,y):

    for i in range(x, y):
        nona = opening.iloc[0:, [i, 49]].dropna()
        if nona.empty:
            print 'no coordinate'
            break
        linreg.fit(nona['height'].values.reshape(-1, 1), nona.iloc[:, [0]])  # because Rhip has one dimension
        #a, b = linreg.coef_, linreg.intercept_

        myheight= np.array(MYHEIGHT).reshape(-1, 1)
        print linreg.predict(myheight)


def closecoordinate(x,y):

    for i in range(x, y):
        nona = close.iloc[0:, [i, 49]].dropna()
        if nona.empty:
            print 'no coordinate'
            break
        linreg.fit(nona['height'].values.reshape(-1, 1), nona.iloc[:, [0]])  # because Rhip has one dimension
        #a, b = linreg.coef_, linreg.intercept_

        myheight= np.array(MYHEIGHT).reshape(-1, 1)
        print linreg.predict(myheight)

################left3higt###################### left hand
#frame 265 [column 264-150=114] bottom hight ----1st time ---open pose
#frame 464 [column 463-150=313] bottom hight ----2st time ---open pose
#frame 681 [column 680-150=530] bottom hight ----3st time ---open pose

print '\n'
print 'highest, left hand "start to open" pose:\n'
print '\n'

count=1
for j in range(16):
    print '\n'
    print 'the prediction coordinate of ',name[j],":\n",
    opencoordinate(count, count+3)
    count=(j+1)*3+1


#frame 295 [column 294-150=144] bottom hight ----1st time ---opening
#frame 486 [column 485-150=335] bottom hight ----2st time ---opening
#frame 706 [column 705-150=555] bottom hight ----3st time ---opening
print '\n'
print 'highest, left hand opening pose:\n'
print '\n'

count1=1
for j in range(16):
    print '\n'
    print 'the prediction coordinate of ',name[j],":\n",
    openingcoordinate(count1, count1+3)
    count1=(j+1)*3+1


#frame 323 [column 322-150=172] bottom hight ----1st time ---close
#frame 516 [column 515-150=365] bottom hight ----2st time ---close
#frame 738 [column 737-150=587] bottom hight ----3st time ---close
print '\n'
print 'highest, left hand close pose:\n'
print '\n'

count2=1
for j in range(16):
    print '\n'
    print 'the prediction coordinate of ',name[j],":\n",
    closecoordinate(count2, count2+3)
    count2=(j+1)*3+1