'''
Created on Oct 26, 2014

@author: user
'''
import os, sys, inspect, time  # @UnusedImport
sys.path.insert(0, 'C:\Users\user\Anaconda\Lib\site-packages')
import numpy as np
from sklearn import metrics
import Spectral, Connectivity, Dunn_index

name = '\LCSS_Sunday_Spectral'
dist_name = '\LCSS_distMat-Sunday.txt'
data_name = '\Sunday-clean.csv'
path = 'C:\Users\user\workspace\Results' 
if not os.path.exists(path+name):os.makedirs(path+name)
 
'''***************Load data***************'''
##################################################################
path ='C:\Users\user\workspace'
 
start = time.time()
print "loading data"
dist = np.loadtxt(path+'\Results'+dist_name,delimiter = ' ')  # @UndefinedVariable
#data = np.loadtxt(path+data_name,delimiter = ',')  # @UndefinedVariable
Aff = 1-dist
end = time.time()
print "load time is %s seconds " %str(int(end-start))

#===============================================================================
# m = data.shape[0]
# n = data.shape[1]
# 
# clean_data = []
# flag = 0
# for i in range(m):
#     if data[i,0]==1 and list(data[i,:]).count(1)+list(data[i,:]).count(0)<n-3:
#         if flag==0:
#             flag = 1
#             clean_data = data[i,:]
#         else:
#             clean_data = np.vstack([clean_data,data[i,:]])
# 
# print clean_data.shape[0]        
# np.savetxt(path+'\clean_data.csv', clean_data,delimiter=",")  # @UndefinedVariable
#===============================================================================


scores = np.zeros((25,4))
 
for k in range(1,26):
    print "=============================="
    start = time.time()
    labels = Spectral.Spectral(Aff,k*2)
    np.savetxt(path+'\Results\LCSS_Sunday_Spectral\k='+str(k*2)+' clusters.txt', labels)  # @UndefinedVariable
    model = time.time()
    print "Model time is %s seconds " %(str(int(model-start)))
    scores[k-1,0] = k*2
    Dunn_score = Dunn_index.Dunn(labels,dist)
    scores[k-1,1] = Dunn_score
    Dunn_time = time.time()
    print "Dunn time is %s seconds " %(str(int(Dunn_time-start)))
    sil_score = metrics.silhouette_score(dist, labels, metric='precomputed')
    scores[k-1,2] = sil_score
    Sil_time = time.time()
    print "Silhouette time is %s seconds " %(str(int(Sil_time-Dunn_time)))
    Conn_score = Connectivity.Conn(labels, dist)
    scores[k-1,3] = Conn_score
    Conn_time = time.time()
    print "Connectivity time is %s seconds " %(str(int(Conn_time-Sil_time)))
print scores
np.savetxt(path+'\Results\LCSS_Sunday_Spectral\\new_Scores.csv', scores)  # @UndefinedVariable

