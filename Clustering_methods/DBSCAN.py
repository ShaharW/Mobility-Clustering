'''
Created on Oct 30, 2014

@author: user
'''

def DBSCAN(dist,epsilon=0.5,min_samp = 10):
    '''***************Imports****************'''
    ##################################################################
    import os, sys, inspect, time  # @UnusedImport
    sys.path.insert(0, 'C:\Users\user\Anaconda\Lib\site-packages')
    from sklearn.cluster import DBSCAN  # @UnresolvedImport @UnusedImport
    
    ##################################################################
    
    '''***************DBSCAN***************'''
    ##################################################################

    print "clustering with DBSCAN"
    end = time.time()
    estimator = DBSCAN(eps=epsilon, min_samples=min_samp, metric='precomputed')
    labels = estimator.fit_predict(dist)
    ##################################################################
    
    end2 = time.time()
    print "model time is %s seconds " %str(int(end2-end))
    print "%s clusters found" %str(len(set(labels)))
    return len(set(labels)), labels + 1 # return # of clusters and labels
