'''
Created on Dec 7, 2014

@author: Shahar Weinstock

Calculating the normalized KL distance between each pair of Markov models.
First, the KL measure between each row is being summed to a total distance between the models.
Second, the distances are being normalized to 0-1 range by dividing with the max distance.

'''
import os, sys, inspect, time  # @UnusedImport
sys.path.insert(0, 'C:\Users\user\Anaconda\Lib\site-packages')
from scipy import stats
import numpy as np

def HMM_distMat(models):
    distMat = np.zeros((models.shape[0],models.shape[0]))
    for index_a,mat_a in enumerate(models):
        for index_b,mat_b in enumerate(models):
            distMat[index_a,index_b] = sum(stats.entropy(mat_a[i,:],mat_b[i,:]) for i in range(mat_a.shape[0]))
    distMat = distMat/distMat.max()
    return distMat