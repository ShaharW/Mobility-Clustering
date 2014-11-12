'''
Created on Nov 2, 2014

@author: user
'''

def Spectral(dist,k):
    '''***************Imports****************'''
    ##################################################################
    import os, sys, inspect, time  # @UnusedImport
    sys.path.insert(0, 'C:\Users\user\Anaconda\Lib\site-packages')
    from sklearn.cluster import SpectralClustering  # @UnresolvedImport @UnusedImport
    
    ##################################################################
    
    '''***************DBSCAN***************'''
    ##################################################################

    print "clustering with Spectral clustering"
    end = time.time()
    estimator = SpectralClustering(n_clusters=k,affinity='precomputed')
    labels = estimator.fit_predict(dist)
    ##################################################################
    
    end2 = time.time()
    print "model time is %s seconds " %str(int(end2-end))
    print "%s clusters found" %str(len(set(labels)))
    return labels

        
