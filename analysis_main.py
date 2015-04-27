'''
Created on Mar 30, 2015

@author: Shahar Weinstock
'''

import os, sys, inspect, time  # @UnusedImport
sys.path.insert(0, 'C:\Users\user\Anaconda\Lib\site-packages')
from copy import deepcopy
import numpy as np
from sklearn import metrics, cluster
from My_methods import Entropy, Markov, Markov_JS_distMat
from Clustering_methods import Agglomerative,Kmedoids,DBSCAN,Spectral,EM
from Literature_methods import LCSS_distMat, Euclidean_distMat
from sklearn.decomposition import PCA
from scipy import stats

'''************Initializeing Parameters**************'''
#name = '\\PCA'
#name = '\\EM'
name = '\\1MM'
#name = '\\LCSS'
#name = '\\Data'
#dist_name = '\\1MM_JS_distMat.txt'
dist_name = '\LCSS_distMat.txt'
#models_name = '\models_new.npy'
data_name = '\weekdays.csv'
#labels_name = '\Results\labels'
path = 'C:\Users\User\workspace\Results\Analysis' 
#if not os.path.exists(path+name):os.makedirs(path+name)
 
##################################################################
factor = 0.0
iterations = 1
analysis_type = 'time'

'''***************Load data***************'''
#data = np.loadtxt(path+data_name,delimiter = ',')  # @UndefinedVariable
#data = np.loadtxt(path+'\\Data\\factor = '+str(factor)+','+analysis_type+','+'data.csv', delimiter=",")
#===============================================================================
# cnt = 0
# print str(cnt),
# while True:
#     time.sleep( 5 )
#     cnt += 1
#     print "\n" + str(cnt),
#===============================================================================
ret = np.zeros(2)


for iter in range(iterations):
    #factor = iter*0.1
    print name+ ", "+analysis_type+", factor = "+str(factor)
    ''' adding noise '''
    #===========================================================================
    # analysis_type  = "existing noise"
    # factor = 0.46 + 0.07*iter
    # print analysis_type+", factor = "+str(factor)+", iteration = "+str(iter+1)
    # for i in range(data.shape[0]):
    #     if np.random.rand() < factor:
    #         indel = data[i,round(np.random.rand()*(data.shape[1]-1))]
    #         data[i,np.random.random_integers(0, data.shape[1]-1)] = indel
    #===========================================================================

    ''' Indel '''
    #===========================================================================
    # analysis_type  = "indel-replace"
    # factor = 0.07+iter*0.07
    # print analysis_type+", factor = "+str(factor)+", iteration = "+str(iter+1)
    # s = data.shape[1] #hours in week
    # t = 5             #days in week
    # for i in range(data.shape[0]):
    #     if np.random.rand() < factor:
    #         interval = np.random.random_integers(1, 3)
    #         cut_location = np.random.random_integers(0,s/t-1-interval)
    #         paste_location = np.random.random_integers(0,s/t-1-interval)
    #         while np.abs(cut_location-paste_location)<interval:
    #             paste_location = np.random.random_integers(0,s/t-1-interval)
    #         for j in range(t):
    #             temp = deepcopy(data[i,j*(s/t)+cut_location:j*(s/t)+cut_location+interval])
    #             data[i,j*(s/t)+cut_location:j*(s/t)+cut_location+interval] = data[i,j*(s/t)+paste_location:j*(s/t)+paste_location+interval]
    #             data[i,j*(s/t)+paste_location:j*(s/t)+paste_location+interval] = temp
    #===========================================================================
     
    ''' moving in time '''
    #===========================================================================
    # analysis_type  = "time"
    # print analysis_type+", factor = "+str(factor)+", iteration = "+str(iter+1)
    # for i in range(data.shape[0]):
    #     print i
    #     if np.random.rand() < factor:
    #         interval = 2 #np.random.random_integers(1, 3)
    #         if np.random.rand() < 0.5:
    #             temp = deepcopy(data[i,0:interval])
    #             data[i,0:data.shape[1]-interval] = data[i,interval:data.shape[1]]
    #             data[i,data.shape[1]-interval:] = temp
    #         else:
    #             temp = deepcopy(data[i,data.shape[1]-interval:])
    #             data[i,interval:] = data[i,0:data.shape[1]-interval]
    #             data[i,0:interval] = temp
    # np.savetxt(path+name+'\\factor = '+str(factor)+','+analysis_type+','+'data.csv', data, delimiter=",")
    #===========================================================================
      
                
    ''' LCSS distMat '''
    if name == '\\LCSS':
        dist = np.loadtxt(path+name+'\\distMat\\factor = '+str(factor)+','+analysis_type+','+'distMat.txt',delimiter = " ")
        #=======================================================================
        # dist = LCSS_distMat.LCSS_distMat(data)
        # np.savetxt(path+name+'\\distMat\\factor = '+str(factor)+','+analysis_type+','+'distMat.txt', dist, delimiter=" ")
        #=======================================================================
        
    ''' Markov distMat '''
    if name == '\\1MM':
        dist = np.loadtxt(path+name+'\\distMat\\factor = '+str(factor)+','+analysis_type+','+'distMat.txt',delimiter = " ")
        #=======================================================================
        # models = Markov.MM(data, 1)
        # models = np.array(models)
        # dist = Markov_JS_distMat.MM_distMat(models)
        # np.savetxt(path+name+'\\distMat\\factor = '+str(factor)+','+analysis_type+','+'distMat.txt', dist, delimiter=" ")
        #=======================================================================
        
    ''' PCA distMat '''
    if name == '\\PCA':
        dist = np.loadtxt(path+name+'\\distMat\\factor = '+str(factor)+','+analysis_type+','+'distMat.txt',delimiter = " ")
        #=======================================================================
        # pca_data = np.zeros((data.shape[0],data.shape[1]*7))
        # for i in range(data.shape[0]):
        #     for j in range(data.shape[1]):
        #         pca_data[i,data[i,j]*23+j] = 1
        # pca = PCA(n_components=7)
        # new_data = pca.fit_transform(pca_data)
        # dist = Euclidean_distMat.distMat(new_data)
        # np.savetxt(path+name+'\\factor = '+str(factor)+','+analysis_type+','+'distMat.txt', dist, delimiter=" ")
        #=======================================================================
        
    ''' Clustering '''
    true_labels = np.loadtxt(path+ name+"\\k=30 clusters.txt")
   
    base_scores = np.loadtxt(path+name+"\\base_scores.csv",delimiter = ',')
    scores = np.zeros([50,2])
      
    for i in range(50):
        print 'clustering iteration - '+str(i)
        k=30
        if name == '\\EM':
            labels = EM.EM(data, k)
        else:
            labels = Kmedoids.Kmedoids(dist, k)
            #np.savetxt(path+name+'\\k='+str(i)+' clusters.txt', labels,delimiter=" ")
  
        scores[i,0] = metrics.v_measure_score(true_labels, labels)
        scores[i,1] = metrics.adjusted_rand_score(true_labels, labels)
        #print scores[i,:]
    #=======================================================================
    # print stats.mstats.normaltest(scores[:,0])[1]
    # print stats.mstats.normaltest(scores[:,1])[1]
    # print stats.mstats.normaltest(scores[:,2])[1]
    #=======================================================================
    np.savetxt(path+name+'\\base_scores.csv', scores,fmt='%.50f', delimiter=",")
  
    ret[0] = stats.ttest_ind(base_scores[:,0],scores[:,0], equal_var = False)[1]
    ret[1] = stats.ttest_ind(base_scores[:,1],scores[:,1], equal_var = False)[1]
    np.savetxt(path+name+'\\factor = '+str(factor)+','+analysis_type+'.csv', ret.reshape((1,2)),fmt='%.50f', delimiter=",")


  
''' Create data for analysis '''
#===============================================================================
# k = 50
# markov_labels = np.loadtxt("C:\Users\User\workspace\Results\Weekdays\\1MM\Labels\Kmedoids\k="+str(k)+" clusters.txt",delimiter = ' ')  # @UndefinedVariable
# LCSS_labels = np.loadtxt("C:\Users\User\workspace\Results\Weekdays\LCSS\Labels\Kmedoids\k="+str(k)+" clusters.txt",delimiter = ' ')  # @UndefinedVariable
# 
# def find_clusters(labels):
#     clusters = []
#     for l in range(k):
#         new_cluster = []
#         for i in range(len(labels)):
#             if labels[i] == l:
#                 new_cluster.append(i)
#         clusters.append(new_cluster)
#     return clusters
# 
# def mutual_clusters(clustersA,clustersB):
#     clusters = []
#     for a in range(k):
#         new_cluster = []
#         max = 0
#         for b in range(k):
#             inter = list(set(clustersA[a]).intersection(clustersB[b]))
#             if len(inter) > max:
#                 new_cluster = inter
#                 max = len(inter)
#         if max >= 30:
#             clusters.append(new_cluster)
#         else:
#             clusters.append([])
#     return clusters
# 
# markov_clusters = find_clusters(markov_labels)
# LCSS_clusters = find_clusters(LCSS_labels)
# 
# intersect = mutual_clusters(markov_clusters, LCSS_clusters)
# 
# labels = np.zeros(len(markov_labels))
# label = 0
# for i in range(k):
#     counter = 0
#     if len(intersect[i]) > 0:
#         label += 1
#     for j in intersect[i]:
#         labels[j] = label
#         counter += 1
#         if counter == 30:
#             break
# 
# np.savetxt("C:\Users\User\workspace\Results\Analysis\labels.txt",labels,fmt='%.1f', delimiter=',')  # @UndefinedVariable 
#===============================================================================
