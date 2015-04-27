'''
Created on Sep 9, 2014

@author: Shahar Weinstock
'''
import os, sys, inspect, time  # @UnusedImport
sys.path.insert(0, 'C:\Users\user\Anaconda\Lib\site-packages')
import numpy as np
import LCSS

def LCSS_distMat(data):
    start = time.time()
    length, width = data.shape
    width *= 1.0
    dist = np.zeros((length,length))
    for i in xrange(length):
        #print "instance - " + str(i)
        for j in xrange(i+1):
            dist[i,j] = 1-LCSS.lcs(data[i,:],data[j,:])/width
            dist[j,i] = dist[i,j]
    dist = dist/dist.max() # normalize
    #print "normalization OFF"
    end = time.time()
    #print "calculation time is %s seconds " %str(int(end-start))
    return dist