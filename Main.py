'''
Created on Oct 26, 2014

@author: user
'''
import os, sys, inspect, time  # @UnusedImport
sys.path.insert(0, 'C:\Users\user\Anaconda\Lib\site-packages')
import numpy as np
from sklearn import metrics, cluster
from My_methods import Entropy, Markov, Markov_JS_distMat
from Clustering_methods import Agglomerative,Kmedoids,DBSCAN,Spectral,EM
#from Literature_methods import LCSS_distMat
from Internal_validity_indices import Connectivity, Dunn_index
from sklearn.decomposition import PCA
from Literature_methods import Euclidean_distMat

'''************Initializeing Parameters**************'''
name = '\\1MM'
#name = '\EM'
#name = '\PCA'
#name = '\\LCSS'
dist_name = '\\1MM_JS_distMat-new.txt'
#dist_name = '\LCSS_distMat_noOnes.txt'
#models_name = '\models.npy'
data_name = '\weekdays.csv'
#labels_name = '\LCSS'
path = 'C:\Users\User\workspace\Results\Weekdays' 
if not os.path.exists(path+name):os.makedirs(path+name)
 
'''***************Load data***************'''
##################################################################
start = time.time()
print "loading data"
dist = np.loadtxt(path+name+dist_name,delimiter = ' ')  # @UndefinedVariable
#Aff = np.loadtxt(path+name+"\Aff.txt",delimiter = ' ') 
#data = np.loadtxt(path+data_name,delimiter = ',')  # @UndefinedVariable
#models = np.load(path+name+models_name)  # @UndefinedVariable
Aff = np.exp(-2 * dist / dist.std())
#Aff = 1-dist
#dist = np.loadtxt('C:\Users\User\workspace\Results\Weekdays\Hamming.txt',delimiter = ' ')  # @UndefinedVariable
#Aff = np.exp(-2 * dist / dist.std())
end = time.time()
print "load time is %s seconds " %str(int(end-start))


''' Create data for PCA '''
#===============================================================================
# new_data = np.zeros((data.shape[0],161))
#  
# for i in range(data.shape[0]):
#     for j in range(data.shape[1]):
#         new_data[i,data[i,j]*23+j] = 1
# np.savetxt(path+'\PCA_Sunday_data.csv', new_data, delimiter=",")  # @UndefinedVariable
#===============================================================================

''' LCSS distMat '''
#===============================================================================
# dist = LCSS_distMat.LCSS_distMat(data)
# np.savetxt(path+name+'\\LCSS_distMat.txt', dist, delimiter=" ")  # @UndefinedVariable
#===============================================================================

''' Markov models '''
#===============================================================================
# models = Markov.MM(data, 3)
# np.save(path+name+'\models', models)  # @UndefinedVariable
#===============================================================================

''' Markov distMat '''
#===============================================================================
# dist = Markov_JS_distMat.MM_distMat(models)
# np.savetxt(path+name+'\\3MM_JS_distMat-new.txt', dist, delimiter=" ")  # @UndefinedVariable
#===============================================================================

''' evaluate clustering '''
#===============================================================================
# methods = ["\\3Markov","\Markov","\EM","\LCSS"]
# for method in methods:
#     labels = np.loadtxt(path+labels_name +method +".txt",delimiter = ',')  # @UndefinedVariable
#     print "Entropy measure for "+method+ " is - " +str(Entropy.evaluation(data, labels, 2))
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
# scores = np.zeros((19,6))
#     
# for i in range(19):
#     print "=============================="
#     epsilon = 0.01 + 0.01*i
#     print "epsilon = " + str(epsilon)
#     start = time.time()
#     model = DBSCAN.DBSCAN(dist, epsilon)
#     labels = model[1]
#     k = model[0]
#     np.savetxt(path+name+'\epsilon = '+str(epsilon)+", k = "+str(k)+'.txt', labels, fmt='%i')  # @UndefinedVariable
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
#     Ent_score = Entropy.evaluation(data, labels, 2)
#     scores[i,5] = Ent_score
#     Ent_time = time.time()
#     print "Entropy time is %s seconds " %(str(int(Ent_time-Conn_time)))
# print scores
# np.savetxt(path+name+'DBSCAN\DBSCAN_Scores.csv', scores,fmt='%.2f', delimiter=',')  # @UndefinedVariable
#===============================================================================

#===============================================================================
# labels = Spectral.Spectral(Aff, 100)
# Ent_score = Entropy.evaluation(data, labels, 2)
# print "entropy is - " + str(Ent_score)
# np.savetxt(path+'\k='+str(100)+' LCSS.txt', labels, fmt='%.2f')  # @UndefinedVariable
#===============================================================================

#===============================================================================
# labels = np.zeros(data.shape[0])
# Ent_score = Entropy.evaluation(data, labels, 3)
# print Ent_score
#=============================================================================== 0 



''' PCA ''' 
#===============================================================================
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from sklearn.cluster import DBSCAN
#    
# #pca_data = np.loadtxt(path+name+"\PCA_data.csv",delimiter = ',')  # @UndefinedVariable
#       
# #print "#################### comp = "+str(7)+" ################"
# #pca = PCA(n_components=7)
# #new_data = pca.fit_transform(pca_data)
# 
#   
# #estimator = cluster.KMeans(n_clusters=2)    
# #labels = estimator.fit(new_data).predict(new_data)
# #estimator = DBSCAN(1.7,20)
# #labels = estimator.fit_predict(new_data)
# 
# #===============================================================================
# # fig = plt.figure()
# #   
# # colors = ["r", "b", "g","y","g","k","w"]
# # for i in range(len(labels)):
# #     plt.scatter(new_data[i,0],new_data[i,1],c=colors[labels[i]])
# # plt.xlabel('1st PC')
# # plt.ylabel('2nd PC')
# #   
# # plt.show()
# # np.savetxt(path+name+'\explained variance ratio.csv', pca.explained_variance_ratio_, fmt='%.3f', delimiter=',')  # @UndefinedVariable  
# #===============================================================================
#scores = np.zeros((99,4))
           
''' clustering '''
for k in range(2,101):
    print "=============================="
    print "K = " + str(k)
    start = time.time()
    #labels = np.loadtxt(path+name+'\Labels\k='+str(k)+' clusters.txt',delimiter = ',') 
    labels = Kmedoids.Kmedoids(dist, k)
    np.savetxt(path+name+'\Labels\Kmedoids\k='+str(k)+' clusters.txt', labels,fmt='%i', delimiter=" ")
    model = time.time()
    print "Model time is %s seconds " %(str(int(model-start)))
#===============================================================================
#     scores[k-2,0] = k
#     Dunn_score = Dunn_index.Dunn(labels,dist)
#     scores[k-2,1] = Dunn_score
#     Dunn_time = time.time()
#     print "Dunn time is %s seconds " %(str(int(Dunn_time-start)))
#     sil_score = metrics.silhouette_score(dist, np.asarray(labels), metric='precomputed')
#     scores[k-2,2] = sil_score
#     Sil_time = time.time() 
#     print "Silhouette time is %s seconds " %(str(int(Sil_time-Dunn_time)))
#     Conn_score = Connectivity.Conn(labels, dist)
#     scores[k-2,3] = Conn_score
#     Conn_time = time.time()
#     print "Connectivity time is %s seconds " %(str(int(Conn_time-Sil_time)))
#     Conn_time = time.time()
#     #===========================================================================
#     # scores[k-2,0] = k
#     # scores[k-2,1] = Entropy.evaluation(data, labels, 1)
#     # scores[k-2,2] = Entropy.evaluation(data, labels, 2)
#     # scores[k-2,3] = Entropy.evaluation(data, labels, 3)
#     # scores[k-2,4] = Entropy.evaluation(data, labels, 4)
#     # scores[k-2,5] = Entropy.evaluation(data, labels, 5)
#     # scores[k-2,6] = Entropy.evaluation(data, labels, 6)
#     # Ent_time = time.time()
#     # print "Entropy time is %s seconds " %(str(int(Ent_time-model)))
#     #===========================================================================
# print scores
# np.savetxt(path+name+'\Scores.csv', scores, fmt='%.3f', delimiter=',')  # @UndefinedVariable'''
#===============================================================================
