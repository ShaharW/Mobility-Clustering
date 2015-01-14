'''
Created on Jan 13, 2015

@author: Shahar Weinstock

Calculating the normalized KL distance between each pair of Markovian models.
The KL divergence between two Markovian models is calculated as KL between joint probability mass functions (Kullback 1959).
The distance between to models is calculated as the Jensen-Shannon divergance.

'''
import os, sys, inspect, time  # @UnusedImport
sys.path.insert(0, 'C:\Users\user\Anaconda\Lib\site-packages')
from scipy import stats
import numpy as np
start = time.time()

def MM_distMat(models):
    distMat = np.zeros((models.shape[0],models.shape[0]))
    nrow = models[0].shape[0]
    ncol = models[0].shape[1] - 1 # the last column is for marginal distribution
    for index_a,mat_a in enumerate(models):
        for index_b,mat_b in enumerate(models[0:index_a]):
            M = 0.5*(mat_a + mat_b)
            Dist_a_M = sum(mat_a[i,ncol]*stats.entropy(mat_a[i,0:ncol],M[i,0:ncol]) for i in range(nrow)) # conditioned KL
            Dist_a_M += stats.entropy(mat_a[:,ncol],M[:,ncol]) # conditioning KL
            Dist_b_M = sum(mat_b[i,ncol]*stats.entropy(mat_b[i,0:ncol],M[i,0:ncol]) for i in range(nrow)) # conditioned KL
            Dist_b_M += stats.entropy(mat_b[:,ncol],M[:,ncol]) # conditioning KL
            distMat[index_a,index_b] = 0.5*(Dist_a_M + Dist_b_M) # according to j-s
            distMat[index_b,index_a] = distMat[index_a,index_b] # symmetric
        print "calculated " + str(int((index_a*(index_a+1))*100/(models.shape[0]*(models.shape[0]+1)))) + "% in " + str(int((time.time()-start)/60)) + " minutes"
    distMat = distMat/distMat.max()
    return distMat