'''
Created on Dec 7, 2014

@author: Shahar Weinstock

Calculating the normalized KL distance between each pair of Markovian models.
The KL divergence between two Markovian models is calculated as KL between joint probability mass functions (Kullback 1959)

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
        print "calculating row " + str(index_a) + " out of " + str(models.shape[0])
        print "time passed so far: " + str(int((time.time()-start)/60)) + " minutes"
        for index_b,mat_b in enumerate(models):
            distMat[index_a,index_b] = sum(mat_a[i,ncol]*stats.entropy(mat_a[i,0:ncol],mat_b[i,0:ncol]) for i in range(nrow)) # conditioned KL
            distMat[index_a,index_b] += stats.entropy(mat_a[:,ncol],mat_b[:,ncol]) # conditioning KL
    distMat = distMat/distMat.max()
    return distMat