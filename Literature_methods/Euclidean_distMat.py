'''
Created on Apr 20, 2015

@author: Shahar Weinstock
'''
import os, sys, inspect, time  # @UnusedImport
sys.path.insert(0, 'C:\Users\user\Anaconda\Lib\site-packages')
import numpy as np
import scipy
            
def distMat(data):
    start = time.time()
    length, width = data.shape
    width *= 1.0
    dist = np.zeros((length,length))
    for i in xrange(length):
        print "instance - " + str(i)
        for j in xrange(i+1):
            dist[i,j] = scipy.spatial.distance.euclidean(data[i,:],data[j,:])
            dist[j,i] = dist[i,j]
    dist = dist/dist.max() # normalize
    end = time.time()
    print "calculation time is %s seconds " %str(int(end-start))
    return dist