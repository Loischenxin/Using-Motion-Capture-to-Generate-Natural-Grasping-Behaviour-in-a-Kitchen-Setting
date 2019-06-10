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
HIGHTARR=[TOP,MIDDLE,BOTTOM]
arr=[]
myhight=40

#each hight try three times
for j in HIGHTARR:
    for m in range(9):
        arr.append(j)
print arr

leftThree=pd.read_csv('left3hight.csv')
#print leftThree.loc[0:, 'RhipX':'RhipZ' ]


openpose=leftThree.ix[[150,151,152,420,421,422,695,696,697,976,977,978,1252,1253,1254,
                       1490,1491,1492,1754,1755,1756,2119,2120,2121,2417,2418,2419],0:] #opening data
openpose['hight']=arr
openpose=openpose.replace(0, np.nan)

opening=leftThree.ix[[193,194,195,443,444,445,732,733,734,1005,1006,1007,1284,1285,1286,
                      1525,1526,1527,1783,1784,1785,2187,2188,2189,2504,2505,2506],0:] #opening
opening['hight']=arr
opening=opening.replace(0, np.nan)

close=leftThree.ix[[215,216,217,486,487,488,766,767,768,1050,1051,1052,1307,1308,1309,
                    1556,1557,1558,1827,1828,1829,2221,2222,2223,2562,2563,2564],0:] #close
close['hight']=arr
close=close.replace(0, np.nan)

#print openpose
#print opening
#print close

#build regression model ---linear regression
linreg=linear_model.LinearRegression()



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
#######################Rhip####
print '\n'
print 'left hand "start to open" pose:\n'
print 'the prediction coordinate of Right hip:'
for i in range(1,4):
    nona=openpose.iloc[0:, [i,49]].dropna()
    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)
    print linreg.score(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]])

#######################Lhip####
print 'the prediction coordinate of Left hip:'
for i in range(4,7):
    nona=openpose.iloc[0:, [i,49]].dropna()
    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################Lshoulder####
print 'the prediction coordinate of Left shoulder:'
for i in range(7,10):
    nona=openpose.iloc[0:, [i,49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################HLelbow####
print 'the prediction coordinate of Left Upper Arm:'
for i in range(10,13):
    nona=openpose.iloc[0:, [i,49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################Lelbow####
print 'the prediction coordinate of Left elbow:'
for i in range(13,16):
    nona=openpose.iloc[0:, [i,49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################Lhand####
print 'the prediction coordinate of Left hand:'
for i in range(16,19):
    nona=openpose.iloc[0:, [i,49]].dropna()
    print nona

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)




#######################Rshoulder####
print 'the prediction coordinate of right shoulder:'
for i in range(19,22):
    nona=openpose.iloc[0:, [i,49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################HRelbow####
print 'the prediction coordinate of Right Upper Arm:'
for i in range(22,25):
    nona=openpose.iloc[0:, [i,49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################Relbow####
print 'the prediction coordinate of Right elbow:'
for i in range(25,28):
    nona=openpose.iloc[0:, [i,49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################Rhand####
print 'the prediction coordinate of Right hand:'
for i in range(28,31):
    nona=openpose.iloc[0:, [i,49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################Lfeet####
print 'the prediction coordinate of Left feet:'
for i in range(31,34):
    nona=openpose.iloc[0:, [i,49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################Lknee####
print 'the prediction coordinate of Left knee:'
for i in range(34,37):
    nona=openpose.iloc[0:, [i,49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################Lwaist####
print 'the prediction coordinate of Left waist:'
for i in range(37, 40):
    nona = openpose.iloc[0:, [i, 49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1), nona.iloc[:, [0]])  # because Rhip has one dimension
    a, b = linreg.coef_, linreg.intercept_

    myhight = np.array(myhight).reshape(-1, 1)
    print linreg.predict(myhight)

#######################Rwaist####
print 'the prediction coordinate of Right waist:'
for i in range(40, 43):
    nona = openpose.iloc[0:, [i, 49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1), nona.iloc[:, [0]])  # because Rhip has one dimension
    a, b = linreg.coef_, linreg.intercept_

    myhight = np.array(myhight).reshape(-1, 1)
    print linreg.predict(myhight)

#######################Rknee####
print 'the prediction coordinate of Right knee:'
for i in range(43, 46):
    nona = openpose.iloc[0:, [i, 49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1), nona.iloc[:, [0]])  # because Rhip has one dimension
    a, b = linreg.coef_, linreg.intercept_

    myhight = np.array(myhight).reshape(-1, 1)
    print linreg.predict(myhight)

#######################Rfeet####
print 'the prediction coordinate of Right knee:'
for i in range(46, 49):
    nona = openpose.iloc[0:, [i, 49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1), nona.iloc[:, [0]])  # because Rhip has one dimension
    a, b = linreg.coef_, linreg.intercept_

    myhight = np.array(myhight).reshape(-1, 1)
    print linreg.predict(myhight)

#plot graph of right hip
# plt.ylim(-3000,3000)
# plt.scatter(openpose['hight'],openpose.iloc[:,[1]], color='blue')
# plt.scatter(openpose['hight'],openpose.iloc[:,[2]], color='black')
# plt.scatter(openpose['hight'],openpose.iloc[:,[3]], color='red')
# plt.plot(openpose['hight'], linreg.predict(openpose.iloc[:,[1]].values.reshape(-1,1)), color='blue', linewidth=2)
# plt.plot(openpose['hight'], linreg.predict(openpose.iloc[:,[2]].values.reshape(-1,1)), color='black', linewidth=2)
# plt.plot(openpose['hight'], linreg.predict(openpose.iloc[:,[3]].values.reshape(-1,1)), color='red', linewidth=2)
# plt.xlabel('drawer hight (mm)')
# plt.ylabel('Right Hip aix (mm)')
# plt.show()


#frame 195 [column 194] top hight ----1st time ---opening
#frame 445 [column 444] top hight ----2st time ---opening
#frame 734 [column 733] top hight ----3st time ---opening
#frame 1007 [column 1006] middle hight ----1st time ---opening
#frame 1286 [column 1285] middle hight ----2st time ---opening
#frame 1527 [column 1526] middle hight ----3st time ---opening
#frame 1785 [column 1784] bottom hight ----1st time ---opening
#frame 2189 [column 2188] bottom hight ----2st time ---opening
#frame 2506 [column 2505] bottom hight ----3st time ---opening

#######################Rhip####
print '\n'
print 'left hand opening pose:\n'
print 'the prediction coordinate of Right hip:'
for i in range(1,4):
    nona=opening.iloc[0:, [i,49]].dropna()
    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################Lhip####
print 'the prediction coordinate of Left hip:'
for i in range(4,7):
    nona=opening.iloc[0:, [i,49]].dropna()
    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################Lshoulder####
print 'the prediction coordinate of Left shoulder:'
for i in range(7,10):
    nona=opening.iloc[0:, [i,49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################HLelbow####
print 'the prediction coordinate of Left Upper Arm:'
for i in range(10,13):
    nona=opening.iloc[0:, [i,49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################Lelbow####
print 'the prediction coordinate of Left elbow:'
for i in range(13,16):
    nona=opening.iloc[0:, [i,49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################Lhand####
print 'the prediction coordinate of Left hand:'
for i in range(16,19):
    nona=opening.iloc[0:, [i,49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################Rshoulder####
print 'the prediction coordinate of right shoulder:'
for i in range(19,22):
    nona=opening.iloc[0:, [i,49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################HRelbow####
print 'the prediction coordinate of Right Upper Arm:'
for i in range(22,25):
    nona=opening.iloc[0:, [i,49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################Relbow####
print 'the prediction coordinate of Right elbow:'
for i in range(25,28):
    nona=opening.iloc[0:, [i,49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################Rhand####
print 'the prediction coordinate of Right hand:'
for i in range(28,31):
    nona=opening.iloc[0:, [i,49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################Lfeet####
print 'the prediction coordinate of Left feet:'
for i in range(31,34):
    nona=opening.iloc[0:, [i,49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################Lknee####
print 'the prediction coordinate of Left knee:'
for i in range(34,37):
    nona=opening.iloc[0:, [i,49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################Lwaist####
print 'the prediction coordinate of Left waist:'
for i in range(37, 40):
    nona = opening.iloc[0:, [i, 49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1), nona.iloc[:, [0]])  # because Rhip has one dimension
    a, b = linreg.coef_, linreg.intercept_

    myhight = np.array(myhight).reshape(-1, 1)
    print linreg.predict(myhight)

#######################Rwaist####
print 'the prediction coordinate of Right waist:'
for i in range(40, 43):
    nona = opening.iloc[0:, [i, 49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1), nona.iloc[:, [0]])  # because Rhip has one dimension
    a, b = linreg.coef_, linreg.intercept_

    myhight = np.array(myhight).reshape(-1, 1)
    print linreg.predict(myhight)

#######################Rknee####
print 'the prediction coordinate of Right knee:'
for i in range(43, 46):
    nona = opening.iloc[0:, [i, 49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1), nona.iloc[:, [0]])  # because Rhip has one dimension
    a, b = linreg.coef_, linreg.intercept_

    myhight = np.array(myhight).reshape(-1, 1)
    print linreg.predict(myhight)

#######################Rfeet####
print 'the prediction coordinate of Right knee:'
for i in range(46, 49):
    nona = opening.iloc[0:, [i, 49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1), nona.iloc[:, [0]])  # because Rhip has one dimension
    a, b = linreg.coef_, linreg.intercept_

    myhight = np.array(myhight).reshape(-1, 1)
    print linreg.predict(myhight)

#frame 217 [column 216] top hight ----1st time ---close
#frame 488 [column 487] top hight ----2st time ---close
#frame 768 [column 767] top hight ----3st time ---close
#frame 1052 [column 1051] middle hight ----1st time ---close
#frame 1309 [column 1308] middle hight ----2st time ---close
#frame 1558 [column 1557] middle hight ----3st time ---close
#frame 1829 [column 1828] bottom hight ----1st time ---close
#frame 2223 [column 2222] bottom hight ----2st time ---close
#frame 2564 [column 2563] bottom hight ----3st time ---close


#######################Rhip####
print '\n'
print 'left hand close pose:\n'
print 'the prediction coordinate of Right hip:'
for i in range(1,4):
    nona=close.iloc[0:, [i,49]].dropna()
    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################Lhip####
print 'the prediction coordinate of Left hip:'
for i in range(4,7):
    nona=close.iloc[0:, [i,49]].dropna()
    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################Lshoulder####
print 'the prediction coordinate of Left shoulder:'
for i in range(7,10):
    nona=close.iloc[0:, [i,49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################HLelbow####
print 'the prediction coordinate of Left Upper Arm:'
for i in range(10,13):
    nona=close.iloc[0:, [i,49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################Lelbow####
print 'the prediction coordinate of Left elbow:'
for i in range(13,16):
    nona=close.iloc[0:, [i,49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################Lhand####
print 'the prediction coordinate of Left hand:'
for i in range(16,19):
    nona=close.iloc[0:, [i,49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################Rshoulder####
print 'the prediction coordinate of right shoulder:'
for i in range(19,22):
    nona=close.iloc[0:, [i,49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################HRelbow####
print 'the prediction coordinate of Right Upper Arm:'
for i in range(22,25):
    nona=close.iloc[0:, [i,49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################Relbow####
print 'the prediction coordinate of Right elbow:'
for i in range(25,28):
    nona=close.iloc[0:, [i,49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################Rhand####
print 'the prediction coordinate of Right hand:'
for i in range(28,31):
    nona=close.iloc[0:, [i,49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################Lfeet####
print 'the prediction coordinate of Left feet:'
for i in range(31,34):
    nona=close.iloc[0:, [i,49]].dropna()
    # print nona
    if nona.empty:
        print 'no coordinate'
        break

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################Lknee####
print 'the prediction coordinate of Left knee:'
for i in range(34,37):
    nona=close.iloc[0:, [i,49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1),nona.iloc[:,[0]]) #because Rhip has one dimension
    a,b=linreg.coef_,linreg.intercept_


    myhight=np.array(myhight).reshape(-1,1)
    print linreg.predict(myhight)

#######################Lwaist####
print 'the prediction coordinate of Left waist:'
for i in range(37, 40):
    nona = close.iloc[0:, [i, 49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1), nona.iloc[:, [0]])  # because Rhip has one dimension
    a, b = linreg.coef_, linreg.intercept_

    myhight = np.array(myhight).reshape(-1, 1)
    print linreg.predict(myhight)

#######################Rwaist####
print 'the prediction coordinate of Right waist:'
for i in range(40, 43):
    nona = close.iloc[0:, [i, 49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1), nona.iloc[:, [0]])  # because Rhip has one dimension
    a, b = linreg.coef_, linreg.intercept_

    myhight = np.array(myhight).reshape(-1, 1)
    print linreg.predict(myhight)

#######################Rknee####
print 'the prediction coordinate of Right knee:'
for i in range(43, 46):
    nona = close.iloc[0:, [i, 49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1), nona.iloc[:, [0]])  # because Rhip has one dimension
    a, b = linreg.coef_, linreg.intercept_

    myhight = np.array(myhight).reshape(-1, 1)
    print linreg.predict(myhight)

#######################Rfeet####
print 'the prediction coordinate of Right feet:'
for i in range(46, 49):
    nona = close.iloc[0:, [i, 49]].dropna()

    linreg.fit(nona['hight'].values.reshape(-1, 1), nona.iloc[:, [0]])  # because Rhip has one dimension
    a, b = linreg.coef_, linreg.intercept_

    myhight = np.array(myhight).reshape(-1, 1)
    print linreg.predict(myhight)