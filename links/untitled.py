import MySQLdb
import numpy as np
from numpy.linalg import *
from itertools import combinations
from sklearn.cluster import KMeans


count = 7
points = 3

db = MySQLdb.connect("localhost","root","root","wifi",charset='utf8')
cursor = db.cursor()
sql = "SELECT ReceivedUUID from ap where Counter=%d and Addrflag=0" % count

def search(ReceivedUUID):
        xs = []
        ys = []
        distance = []
        templist = []
        resultlist = []
        sql2 = "SELECT Longitude FROM location WHERE ReceivedUUID='%s'" % ReceivedUUID
        sql3 = "SELECT Lantitude FROM location WHERE ReceivedUUID='%s'" % ReceivedUUID
        sql4 = "SELECT Level FROM location WHERE ReceivedUUID='%s'" % ReceivedUUID
        # 获得距离，经纬度列表
        cursor.execute(sql2)
        esults2 = cursor.fetchall()
        for row2 in results2:
                ys.append(float(row2[0]))
        cursor.execute(sql3)
        results3 = cursor.fetchall()
        for row3 in results3:
                xs.append(float(row3[0]))
        cursor.execute(sql4)
        results4 = cursor.fetchall()
        for row4 in results4:
                ds = pow(10,((-int(row4[0])-35)/(10*n)))
                distance.append(ds)

        # 将距离经纬度合并
        for i in xrange(0,count+1):
                templist.append(xs[i])
                templist.append(ys[i])
                templist.append(distance[i])
                resultlist.append(templist)

        return list(combinations(resultlist,3))


def three_points_cal(locationlist):
        xs = []
        ys = []
        xlie = []
        ylie = []
        distance = []
        addrs = []
        for i in list:
                xs = []
                ys = []
                xlie = []
                ylie = []
                distance = []
                for j in xrange(0,points):
                        xs.append(i[j][0])
                        ys.append(i[j][1])
                        distance.append(i[j][2])
                for i in xrange(0,points):
                        xlie.append(2*(xs[i] - xs[points]))
                for i in xrange(0,points):
                        ylie.append(2*(ys[i] - ys[points]))
                arr = [xlie,ylie]
                AT = array(arr)
                A = AT.transpose()

                for i in xrange(0,points):
                        result = pow(xs[i],2) - pow(xs[points-1],2) + pow(ys[i],2) - pow(ys[points-1],2) + pow(distance[points-1]*0.00001,2) - pow(distance[i]*0.00001,2)
                        b.append(result)
                AT = mat(AT)
                b = mat(b)
                A = mat(A)
                b = b.transpose()
                addr = inv(AT*A)*AT*b
                addr.append(addr[0,0])
                addr.append(addr[1,0])
                addrs.append(addr)    
        return addrs

def K_means(addrlist):
        dataSet = array(list)
        dataSet = dataSet.transpose()
        kmeans = KMeans(n_clusters=1, random_state=0).fit(dataSet)
        center = kmeans.cluster_centers_
        df_center = pd.DataFrame(center, columns=['x', 'y'])
        labels = kmeans.labels_
        print df_center.loc[:,'x']
        print df_center.loc[:,'y']





try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
                ReceivedUUID = row[0]
                pointsList = search(ReceivedUUID)
                addrs = three_points_cal(pointsList)



                # 对数据库进行更新操作
                insql = "update ap set APlongitude='%s' where ReceivedUUID='%s'" % (str(longitude),ReceivedUUID)
                insql2 = "update ap set APlantitude='%s' where ReceivedUUID='%s'" % (str(lantitude),ReceivedUUID)
                insql3 = "update ap set Addrflag=1 where ReceivedUUID='%s'" % ReceivedUUID
                cursor.execute(insql)
                db.commit()
                cursor.execute(insql2)
                db.commit()
                cursor.execute(insql3)
                db.commit()

except:
        print "Error"
