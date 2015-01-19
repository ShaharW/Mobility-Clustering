'''
Created on Oct 26, 2014

@author: user
'''
import os, sys, inspect, time  # @UnusedImport
sys.path.insert(0, 'C:\Users\user\Anaconda\Lib\site-packages')
import numpy as np
from sklearn import metrics
# from My_methods import Markov_JS_distMat
# from Clustering_methods import DBSCAN
# from Literature_methods import LCSS_distMat
from Internal_validity_indices import Connectivity, Dunn_index

name = '\JS_DBSCAN'
dist_name = '\\3MM_JS_distMat.txt'
# models_name = '\\1MM_Sunday.npy'
# data_name = '\Sunday-clean.csv'
path = 'C:\Users\user\workspace\Results\\3MM' 
if not os.path.exists(path+name):os.makedirs(path+name)
 
'''***************Load data***************'''
##################################################################
start = time.time()
print "loading data"
dist = np.loadtxt(path+dist_name,delimiter = ' ')  # @UndefinedVariable
# data = np.loadtxt(path+data_name,delimiter = ',')  # @UndefinedVariable
# models = np.load(path+models_name)  # @UndefinedVariable
Aff = 1-dist
end = time.time()
print "load time is %s seconds " %str(int(end-start))

#===============================================================================
# dist = Markov_JS_distMat.MM_distMat(models)
# np.savetxt(path+name+'\\1MM_JS_distMat.txt', dist, delimiter=" ")  # @UndefinedVariable
#===============================================================================

''' Create Sunday data '''
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

''' Clustering '''

''' DBSCAN '''
#===============================================================================
# scores = np.zeros((19,5))
#   
# for i in range(19):
#     print "=============================="
#     epsilon = 0.01 + 0.01*i
#     print "epsilon = " + str(epsilon)
#     start = time.time()
#     model = DBSCAN.DBSCAN(dist, epsilon)
#     labels = model[1]
#     k = model[0]
#     np.savetxt(path+name+'\epsilon = '+str(epsilon)+", k = "+str(k)+'.txt', labels)  # @UndefinedVariable
#     model = time.time()
#     print "Model time is %s seconds " %(str(int(model-start)))
#     scores[i,0] = epsilon
#     scores[i,1] = k
#     Dunn_score = Dunn_index.Dunn(labels,dist)
#     scores[i,2] = Dunn_score
#     Dunn_time = time.time()
#     print "Dunn time is %s seconds " %(str(int(Dunn_time-start)))
#     sil_score = metrics.silhouette_score(dist, np.asarray(labels), metric='precomputed')
#     scores[i,3] = sil_score
#     Sil_time = time.time()
#     print "Silhouette time is %s seconds " %(str(int(Sil_time-Dunn_time)))
#     Conn_score = Connectivity.Conn(labels, dist)
#     scores[i,4] = Conn_score
#     Conn_time = time.time()
#     print "Connectivity time is %s seconds " %(str(int(Conn_time-Sil_time)))
# print scores
# np.savetxt(path+name+'\\Scores.csv', scores, delimiter=',')  # @UndefinedVariable
#===============================================================================


''' Clustering '''
#===============================================================================
# scores = np.zeros((25,4))
#      
# for k in range(1,26):
#     print "=============================="
#     print "K = " + str(k*2)
#     start = time.time()
#     labels = Spectral.Spectral(Aff, k*2)
#     np.savetxt(path+name+'\k='+str(k*2)+' clusters.txt', labels)  # @UndefinedVariable
#     model = time.time()
#     print "Model time is %s seconds " %(str(int(model-start)))
#     scores[k-1,0] = k*2
#     Dunn_score = Dunn_index.Dunn(labels,dist)
#     scores[k-1,1] = Dunn_score
#     Dunn_time = time.time()
#     print "Dunn time is %s seconds " %(str(int(Dunn_time-start)))
#     sil_score = metrics.silhouette_score(dist, np.asarray(labels), metric='precomputed')
#     scores[k-1,2] = sil_score
#     Sil_time = time.time() 
#     print "Silhouette time is %s seconds " %(str(int(Sil_time-Dunn_time)))
#     Conn_score = Connectivity.Conn(labels, dist)
#     scores[k-1,3] = Conn_score
#     Conn_time = time.time()
#     print "Connectivity time is %s seconds " %(str(int(Conn_time-Sil_time)))
# print scores
# np.savetxt(path+name+'\\Scores.csv', scores, delimiter=',')  # @UndefinedVariable
#===============================================================================
