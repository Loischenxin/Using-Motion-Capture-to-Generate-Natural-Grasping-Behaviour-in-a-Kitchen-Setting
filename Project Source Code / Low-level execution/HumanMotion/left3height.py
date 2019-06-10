import csv
import numpy as np
from math import *
import pandas as pd
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import metrics

HIGHT=47.5

BOTTOM=30
MIDDLE=45
TOP=60
HIGHTARR = [TOP,MIDDLE,BOTTOM]
arr = []
MYHIGHT = 45

#each hight try three times
for j in HIGHTARR:
    for m in range(9):
        arr.append(j)
print arr

leftThree=pd.read_csv('left3hight.csv')
#print leftThree.loc[0:, 'RhipX':'RhipZ' ]

name=['RhipX','Lhip','Lshoulder','HLelbow','Lelbow','Lhand',
'Rshoulder','HRelbow','Relbow','Rhand','Lfeet','Lknee',
      'Lwaist','Rwaist','Rknee','Rfeet']
openpose=leftThree.ix[[150,151,152,420,421,422,695,696,697,976,977,978,1252,1253,1254,
                       1490,1491,1492,1754,1755,1756,2119,2120,2121,2417,2418,2419],0:] #opening data
openpose['height']=arr
openpose=openpose.replace(0, np.nan)

opening=leftThree.ix[[193,194,195,443,444,445,732,733,734,1005,1006,1007,1284,1285,1286,
                      1525,1526,1527,1783,1784,1785,2187,2188,2189,2504,2505,2506],0:] #opening
opening['height']=arr
opening=opening.replace(0, np.nan)

close=leftThree.ix[[215,216,217,486,487,488,766,767,768,1050,1051,1052,1307,1308,1309,
                    1556,1557,1558,1827,1828,1829,2221,2222,2223,2562,2563,2564],0:] #close
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
        linreg.fit(nona['height'].values.reshape(-1, 1), nona.iloc[:, [0]])  
        # because Rhip has one dimension
        #a, b = linreg.coef_, linreg.intercept_

        myheight= np.array(MYHIGHT).reshape(-1, 1)
        print linreg.predict(myheight)

def openingcoordinate(x,y):

    for i in range(x, y):
        nona = opening.iloc[0:, [i, 49]].dropna()
        if nona.empty:
            print 'no coordinate'
            break
        linreg.fit(nona['height'].values.reshape(-1, 1), nona.iloc[:, [0]])  
        # because Rhip has one dimension
        #a, b = linreg.coef_, linreg.intercept_

        myheight= np.array(MYHIGHT).reshape(-1, 1)
        print linreg.predict(myheight)


def closecoordinate(x,y):

    for i in range(x, y):
        nona = close.iloc[0:, [i, 49]].dropna()
        if nona.empty:
            print 'no coordinate'
            break
        linreg.fit(nona['height'].values.reshape(-1, 1), nona.iloc[:, [0]])  
        # because Rhip has one dimension
        #a, b = linreg.coef_, linreg.intercept_

        myheight= np.array(MYHIGHT).reshape(-1, 1)
        print linreg.predict(myheight)

################left3higt###################### left hand
#frame 152 [column 151] top hight ----1st time ---open pose
#frame 422 [column 421] top hight ----2st time ---open pose
#frame 697 [column 696] top hight ----3st time ---open pose
#frame 978 [column 977] middle hight ----1st time ---open pose
#frame 1254 [column 1253] middle hight ----2st time ---open pose
#frame 1492 [column 1491] middle hight ----3st time ---open pose
#frame 1756 [column 1755] bottom hight ----1st time ---open pose
#frame 2121 [column 2120] bottom hight ----2st time ---open pose
#frame 2419 [column 2418] bottom hight ----3st time ---open pose

print '\n'
print '"start to open" pose:\n'
print '\n'

count=1
for j in range(16):
    print '\n'
    print 'the prediction coordinate of ',name[j],":\n",
    opencoordinate(count, count+3)
    count=(j+1)*3+1

#frame 195 [column 194] top hight ----1st time ---opening
#frame 445 [column 444] top hight ----2st time ---opening
#frame 734 [column 733] top hight ----3st time ---opening
#frame 1007 [column 1006] middle hight ----1st time ---opening
#frame 1286 [column 1285] middle hight ----2st time ---opening
#frame 1527 [column 1526] middle hight ----3st time ---opening
#frame 1785 [column 1784] bottom hight ----1st time ---opening
#frame 2189 [column 2188] bottom hight ----2st time ---opening
#frame 2506 [column 2505] bottom hight ----3st time ---opening
print '\n'
print 'opening pose:\n'
print '\n'

count1=1
for j in range(16):
    print '\n'
    print 'the prediction coordinate of ',name[j],":\n",
    openingcoordinate(count1, count1+3)
    count1=(j+1)*3+1

#frame 217 [column 216] top hight ----1st time ---close
#frame 488 [column 487] top hight ----2st time ---close
#frame 768 [column 767] top hight ----3st time ---close
#frame 1052 [column 1051] middle hight ----1st time ---close
#frame 1309 [column 1308] middle hight ----2st time ---close
#frame 1558 [column 1557] middle hight ----3st time ---close
#frame 1829 [column 1828] bottom hight ----1st time ---close
#frame 2223 [column 2222] bottom hight ----2st time ---close
#frame 2564 [column 2563] bottom hight ----3st time ---close
print '\n'
print 'close pose:\n'
print '\n'

count2=1
for j in range(16):
    print '\n'
    print 'the prediction coordinate of ',name[j],":\n",
    closecoordinate(count2, count2+3)
    count2=(j+1)*3+1


y_test=leftThree.ix[1285,1:]
print y_test
