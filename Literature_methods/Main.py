'''
Created on Oct 26, 2014

@author: user
'''
import os, sys, inspect, time  # @UnusedImport
sys.path.insert(0, 'C:\Users\user\Anaconda\Lib\site-packages')
import numpy as np
from sklearn import metrics
import DBSCAN

#name = '\LCSS_Agglomerative'
dist_name = '\LCSS_distMat-Sunday.txt'
data_name = '\Sunday.txt'
path = 'C:\Users\user\workspace' 
# if not os.path.exists(path+name):os.makedirs(path+name)
 
'''***************Load data***************'''
##################################################################
path ='C:\Users\user\workspace'
 
start = time.time()
print "loading data"
dist = np.loadtxt(path+'\Results'+dist_name,delimiter = ' ')  # @UndefinedVariable
data = np.loadtxt(path+data_name,delimiter = ' ')  # @UndefinedVariable

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


scores = np.zeros((14,2))
labels = DBSCAN.DBSCAN(dist)
np.savetxt(path+'\Results\LCSS_Sunday_DBSCAN.csv', labels,delimiter = ',')  # @UndefinedVariable

# for k in range(2,16):
#     labels = Agglomerative.Agglomerative(dist,k)
#     np.savetxt(path+'\Results\LCSS_Agglomerative\k='+str(k)+' clusters.txt', labels)  # @UndefinedVariable
#     start = time.time()
#     Dunn_score = Dunn_index.Dunn(labels,dist)
#     scores[k-2,1] = Dunn_score
#     end = time.time()
#     print "Dunn time for is %s seconds " %(str(int(end-start)))
#     print "Dunn score - %s" %str(Dunn_score)
#     sil_score = metrics.silhouette_score(dist, labels, metric='precomputed')
#     print "Sil score - %s" %str(sil_score)
#     scores[k-2,0] = sil_score
# 
# print scores
# np.savetxt(path+'\Results\LCSS_Agglomerative_scores.txt', scores)  # @UndefinedVariable
#===============================================================================
# Dunn = []
# for k in range(2,16):
#     start = time.time()
#     labels = np.loadtxt(path+'\Results'+name+"\k="+str(k)+"-means.txt",delimiter = ',')
#     Dunn_score = Dunn_index.Dunn(labels,dist)
#     Dunn.append(Dunn_score)
#     end = time.time()
#     print "Dunn time for %s-means is %s seconds " %(str(k), str(int(end-start)))
#===============================================================================

  
