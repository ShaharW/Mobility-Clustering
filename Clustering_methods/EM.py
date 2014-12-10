'''
Created on Dec 8, 2014

@author: user
'''
import time  # @UnusedImport


def EM(data,k):
    '''***************Imports****************'''
    ##################################################################
    import numpy as np
    from sklearn.mixture import GMM  # @UnresolvedImport

    ##################################################################
    
    '''***************EM***************'''
    ##################################################################
    g = GMM(n_components=k)
    g.fit(data) 
    return g.predict(data)
    
