'''
Created on Dec 7, 2014

@author: user
'''
import os, sys, inspect, time  # @UnusedImport
sys.path.insert(0, 'C:\Users\user\Anaconda\Lib\site-packages')
from scipy import stats
import numpy as np

def HMM_distMat(models):
    distMat = np.zeros((models.shape[0],models.shape[0]))
    for index_a,mat_a in enumerate(models):
        print index_a
        print mat_a
        for index_b,mat_b in enumerate(models):
            [(val = 0.01) for val in mat_b[index] for index, t in enumerate(mat_b) if val == 0]
            distMat[index_a,index_b] = stats.entropy(mat_a,mat_b)
    return distMat