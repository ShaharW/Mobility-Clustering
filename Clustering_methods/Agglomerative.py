'''
Created on Nov 2, 2014

@author: user
'''

def Agglomerative(dist,k):
    '''***************Imports****************'''
    ##################################################################
    from sklearn.cluster import AgglomerativeClustering  # @UnresolvedImport @UnusedImport
    import time
    ##################################################################
    
    '''***************Agglomerative***************'''
    ##################################################################

    print "clustering with Agglomerative clustering"
    end = time.time()
    estimator = AgglomerativeClustering(n_clusters=k, affinity='precomputed',linkage='complete')
    labels = estimator.fit_predict(dist)
    ##################################################################
    
    end2 = time.time()
    print "model time is %s seconds " %str(int(end2-end))
    print "%s clusters found" %str(len(set(labels)))
    return labels